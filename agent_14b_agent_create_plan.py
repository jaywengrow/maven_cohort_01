import os
import json
from datetime import date
from dotenv import load_dotenv
from langfuse.openai import openai
from langfuse import observe, get_client
from landing_page_tools2 import deploy_site, read_webpage, TOOLS

load_dotenv()
llm = openai
langfuse = get_client()

@observe()
def llm_response(history):
    response = llm.responses.create(
        model="gpt-4.1-mini",
        input=history,
        tools=TOOLS
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

            if function_name == "deploy_site":
                result = {"deploy_site": deploy_site(**args)}
            elif function_name == "read_webpage":
                result = {"read_webpage": read_webpage(**args)}

            history += [{"type": "function_call_output",
                            "call_id": tool_call.call_id,
                            "output": json.dumps(result)}]
    return response

def system_prompt():
    return f"""You are a marketing specialist and web designer who creates web landing pages
    for business owners. The business owner will describe their product or service to you,
    and you will produce a live landing page for them.

    You are equipped with a few tools:

    * You are equipped with a read_webpage tool. This is helpful if the user points you to a specific website to use as design inspiration.
    * You are equipped with a deploy_site tool, which accepts a string of HTML/CSS code. This tool deploys the code to a live site.

    After learning from the user what they want, first create a detailed plan - step by step - of how you'll go about creating their landing page. Then, execute your step-by-step plan.

    Today's date is {date.today().strftime("%B %d, %Y")}.

    Go!"""

assistant_message = "Let me help you create a landing page! Describe your product/service."
user_input = input(f"\nAssistant: {assistant_message}\n\nUser: ")

history = [
    {"role": "developer", "content": system_prompt()},
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