import os
import json
from datetime import date
from dotenv import load_dotenv
from langfuse.openai import openai
from langfuse import observe, get_client
from landing_page_tools3 import deploy_site, read_webpage

load_dotenv()
llm = openai
langfuse = get_client()

MAIN_TOOLS = [
    {
        "type": "function",
        "name": "launch_site",
        "description": """Creates a live web landing page, returning
        the URL of that page.""",
        "parameters": {
            "type": "object",
            "properties": {
                "summary": {
                    "type": "string",
                    "description": "The summarized description of the details of the web landing page",
                }
            },
            "required": ["summary"],
        },
    },
    {
        "type": "function",
        "name": "read_webpage",
        "description": "Accesses a webpage and obtains its text.",
        "parameters": {
            "type": "object",
            "properties": {
                "url": {
                    "type": "string",
                    "description": "The URL of the webpage",
                }
            },
            "required": ["url"],
        },
    }
]

@observe()
def launch_site(summary):
    # website design and copy agent
    webpage_text = llm.responses.create(
        model="gpt-4.1-mini",
        input=f"""Below is a brief description of a web landing page
        that is to be created. Craft a detailed outline of the page's
        logical sections, plus the copy that should go in each section.
        
        The landing page should help entice potential customers to purchase
        or sign up for the given product or service. Craft compelling
        copy that achieves this goal.

        Also, describe your vision for the visual design of the site.

        Here are the landing page details: {summary}
        """,
    ).output_text

    # HTML/CSS coding agent
    html = llm.responses.create(
        model="gpt-4.1-mini",
        input=f"""You are an HTML/CSS coder and designer.
        Below is a detailed description of a web landing page
        that is to be created. Write the complete HTML/CSS  
        for the web page.

        Here are the landing page details, including
        copy and design: {webpage_text}
        """,
    ).output_text

    url = deploy_site(html)
    return f"Site is deployed! The URL is: {url}"

@observe()
def llm_response(history):
    response = llm.responses.create(
        model="gpt-4.1-mini",
        input=history,
        tools=MAIN_TOOLS
    )
    return response

@observe()
def agent_loop(history):
    while True:
        response = llm_response(history)
        history += response.output

        tool_calls = [obj for obj in response.output if \
                      getattr(obj, "type", None) == "function_call"]
        text_messages = [obj for obj in response.output if \
                      getattr(obj, "type", None) == "message"]

        if not tool_calls:
            break

        if text_messages:
            print(f"\nAssistant: {response.output_text}")

        for tool_call in tool_calls:
            function_name = tool_call.name
            args = json.loads(tool_call.arguments)
            print(f"TOOL CALL: {function_name} : {args}")

            if function_name == "read_webpage":
                result = {"read_webpage": read_webpage(**args)}
            elif function_name == "launch_site":
                result = {"launch_site": launch_site(**args)}

            history += [{"type": "function_call_output",
                            "call_id": tool_call.call_id,
                            "output": json.dumps(result)}]
    return response

def main_system_prompt():
    return f"""You are a marketing specialist and web designer who creates web landing pages
    for business owners. The business owner will describe their product or service to you,
    and you will produce a live landing page for them.

    Make sure you gather relevant info from the user as to what
    they want. Among the info, you can ask the user if they have
    any external websites they'd like to use as a design
    inspiration. You are equipped with a read_webpage tool
    that allows you to inspect external websites.
   
    When you're ready, summarize what the user wants
    and call your launch_site tool, passing your summary as
    a parameter.

    Go!"""

assistant_message = "Let me help you create a landing page! Describe your product/service."
user_input = input(f"\nAssistant: {assistant_message}\n\nUser: ")

history = [
    {"role": "developer", "content": main_system_prompt()},
    {"role": "assistant", "content": assistant_message},
    {"role": "user", "content": user_input}
]

with langfuse.start_as_current_observation(as_type="span", name="landing-page-conversation") as span:
    while user_input != "exit":
        response = agent_loop(history)
                
        print(f"\nAssistant: {response.output_text}")

        user_input = input("\nUser: ")
        history += [{"role": "user", "content": user_input}]
    
    span.update(output="Conversation complete")

langfuse.flush()

print("****HISTORY****")
print(history)