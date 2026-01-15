import os
import re
import json
import requests
from dotenv import load_dotenv
from langfuse.openai import openai
from langfuse import observe, get_client
from pinecone import Pinecone
from bs4 import BeautifulSoup
from pydantic import BaseModel

load_dotenv()
llm = openai
langfuse = get_client()
pc = Pinecone(api_key=os.getenv("PINECONE_API_KEY"))
dense_index = pc.Index("maven-gross")

MAIN_BOT_TOOLS = [
    {
        "type": "function",
        "name": "research_docs",
        "description": "Retrieves relevant documentation excerpts.",
        "parameters": {}
    },
]

RAG_TOOLS = [
    {
        "type": "function",
        "name": "search_manual",
        "description": """Searches a software documentation manual and 
        retrieves excerpts relevant to a user query.""",
        "parameters": {
            "type": "object",
            "properties": {
                "query": {
                    "type": "string",
                    "description": """A user query for which we 
                    need to search the documentation manual""",
                },
                "top_k": {
                    "type": "integer",
                    "description": """The number of excerpts to retrieve 
                    from the documentation""",
                }
            },
            "required": ["query", "top_k"],
        },
    },
    {
        "type": "function",
        "name": "read_webpage",
        "description": """Reads the text of a web page at a given URL.""",
        "parameters": {
            "type": "object",
            "properties": {
                "url": {
                    "type": "string",
                    "description": "the URL whose web page is to be read",
                }
            },
            "required": ["url"],
        },
    },
]

@observe()
def llm_response(prompt, tools):
    response = llm.responses.create(
        model="gpt-5-mini",
        input=prompt,
        tools=tools
    )
    return response

@observe()
def classify_and_expand(conversation):
    class ConversationData(BaseModel):
        product_name: str
        expanded_query: str

    prompt = (
        f"""You have two tasks, and you must output the results of 
        both tasks at once.
        1. Classify which software product the user is referring to in 
        their final prompt of <conversation> below. Your output should be 
        limited to one of the following choices: [flamehamster, rumblechirp, 
        verbiage++, guineapigment, emrgency, unsure].
        The option of unsure should be used only if you're not certain which 
        software the user is referring to.
        2. Rewrite, in an expanded way, what the user means to ask based on 
        their final prompt of the <conversation> below, taking into account 
        the full context of the conversation.
        
        Here is the conversation: <conversation>{conversation}</conversation>
        """
    )

    response = llm.responses.parse(
        model="gpt-4.1-mini",
        temperature=0,
        input=prompt,
        text_format=ConversationData
    )

    data = response.output_parsed
    return data.product_name, data.expanded_query

@observe()
def read_webpage(url, rag_chunks):
    try:
        response = requests.get(url)
    except requests.exceptions.RequestException:
        return None
    
    soup = BeautifulSoup(response.text, "html.parser")
    text = soup.get_text()
    rag_chunks[url] = text
    return text

@observe()
def search_manual(query, top_k, manual_name, rag_chunks):
    manual_names = ["flamehamster", "rumblechirp", "verbiage++", 
                    "guineapigment", "emrgency"]
    results = dense_index.search(
        namespace="all-gross",
        query={
            "top_k": top_k,
            "inputs": {
                'text': query
            },
            **({"filter": {"manual": manual_name}} \
               if manual_name in manual_names else {})
        }
    )

    for hit in results['result']['hits']:
        fields = hit.get('fields')
        chunk_text = fields.get('chunk_text')
        rag_chunks[hit['_id']] = chunk_text

    return rag_chunks

@observe()
def research_docs(user_input):
    rag_chunks = {}
    manual_name, user_query = \
        classify_and_expand(history[1:] + [user_prompt(user_input)])
    research_history = [{"role": "developer", "content": f"""<overview>You 
        research software documentation to find information to help with 
        users' issues. Your research takes place by using tools. These tools 
        will automatically export your research, so once you've completed 
        your research, just say RESEARCH COMPLETE and nothing else. Your 
        primary tool for doing research is a function called search_manual, 
        in which you pass in a query and retrieve software manual excerpts 
        relevant to that query. The search_manual tool has two 
        arguments: 1. The user query. 2. The top-K (an integer) representing
        the number of relevant excerpts you want to retrieve from the manual. 
        When choosing a top-K, choose between a range of 3 and 10.
        Note that the underlying search engine uses an embedding-based 
        semantic similarity approach under the hood.</overview>

        Here is the user's query that requires research: 
        <user_query>{user_query}</user_query>

        Here is the step-by-step plan you should follow to do your research:
        <plan>
        1. First, run search_manual passing along the literal <user_query> 
        above as the first argument. Do not rephrase it in any way. As to
        choosing the top-K, analyze whether the <user_query> is general 
        or specific. If the <user_query> is specific, you can probably find 
        the answer with a smaller number of excerpts. But if the <user_query> 
        is a broad question, you may need a greater number of excerpts.
        2. After retrieving the initial excerpts, inspect these excerpts and 
        perform an analysis to determine whether further research is needed. 
        Here are factors to consider:
        A. Do the excerpts contain enough information to adequately advise 
        the user on their issue? If not, you'll need to perform another
        search of the manual. When doing so, try rephrasing the query in 
        another way - perhaps new relevant excerpts may be found using this 
        rephrased query.
        B. If 100% of the excerpts contain relevant info, be concerned that 
        there are additional relevant excerpts in the manual that were NOT 
        retrieved. In this case, run another search with a greater top-K.
        3. Answer yes or no to this question:
        Do any of the retrieved documentation excerpts refer to a website URL 
        that may be relevant to help answer the <user_query>? If the answer 
        is yes, use your tool read_webpage which lets you read the text at 
        those URLs. For example, if the user query is about how to use the  
        GuineaPigment PogoStic tool, and the excerpts mention that PogoStic 
        details can be found at https://guineapigment.com/wiki/pogostic, you 
        should call the read_webpage tool for the URL 
        https://guineapigment.com/wiki/pogostic. However, DON'T use the 
        read_webpage tool twice for the same URL.
        4. Answer yes or no to this question: Do the excerpts mention a 
        keyword or concept you don't have information about? If the answer 
        is yes, perform another search on that keyword to learn more about 
        it. This is important, as it may contain important information to 
        help answer the user query. For example, if a documentation excerpt 
        or web page informs you about a technique called 'fletching', and 
        understanding what fletching is important to answer the <user_query> 
        above, do another search on 'fletching' to learn what it means.
        5. Once you have completed your research, just say RESEARCH COMPLETE. 
        Everything you researched and read will automatically be exported by 
        another system.
        </plan>"""}]

    for _ in range(5):  # classic agent loop
        response = llm_response(research_history, RAG_TOOLS)
        research_history += response.output
        tool_calls = [obj for obj in response.output \
                      if getattr(obj, "type", None) == "function_call"]

        if not tool_calls:
            break

        for tool_call in tool_calls:
            function_name = tool_call.name
            args = json.loads(tool_call.arguments)

            if function_name == "search_manual":
                result = {"search_manual": search_manual(**args, manual_name=manual_name, rag_chunks=rag_chunks)}
            elif function_name == "read_webpage":
                result = {"read_webpage": read_webpage(**args, rag_chunks=rag_chunks)}

            research_history += [{"type": "function_call_output",
                                 "call_id": tool_call.call_id,
                                 "output": json.dumps(result)}]
    return rag_chunks

@observe()
def main_system_prompt():
    return {"role": "developer", "content": """<overview>You are an AI 
        customer support technician who is knowledgeable about software 
        products created by the company called GROSS. The products are: 
        * Flamehamster, a web browser.
        * Rumblechirp, an email client.
        * GuineaPigment, a drawing tool for creating/editing SVGs
        * EMRgency, an electronic medical record system
        * Verbiage++, a content management system.

        You represent GROSS, and you are having a conversation with a human 
        user who needs technical support with at least one of these GROSS 
        products.</overview>
        
        <instructions>
        It is critical that you only answer the user based on information 
        found inside the GROSS products' documentation. You have access to a 
        tool called research_docs that can search to find info within this 
        documentation. This search engine retrieves several excerpts from 
        the documentation. Your response to the user can only be based on 
        these documentation excerpts and not your internal knowledge. 
        Important: Use the research_docs tool only once you understand what 
        the user needs.

        Here are more specific instructions to follow:
        * When helping troubleshoot a user's issue, ask a proactive 
        question to help determine what exactly the issue is. 
        * If the user doesn't mention the name of which GROSS software
        they're asking about, proactively ask them which software they're
        using. List out the choices.
        * When asking proactive follow-up questions, ask exactly one 
        question at a time.
        * Do not mention the terms "documentation excerpts" or "excerpts" 
        in your response.
        * Do not use your general knowledge to answer a user query. Only use 
        the documentation excerpts provided by the research_docs tool to 
        advise the user.
        * If you cannot find any advice for the user based on the excerpts, 
        simply apologize and say that you do not know how to help the user 
        at this time.
        * Before you state any point other than a question, think carefully: 
        which excerpt id does the advice come from? Use a special 
        double-brackets notation before your advice to indicate the excerpt 
        id that the advice comes from. 

        For example:
        <example>
        [[flamehamster-chunk-30]]
        Since the Site Identity Button is gray and you are seeing "Your 
        connection is not secure" on all sites, this indicates that 
        Flamehamster is not able to establish secure (encrypted) connections. 
        Normally, the Site Identity Button will be blue or green for secure 
        sites, showing that the connection is encrypted and the site's
        identity is verified.
        </example>

        If you mention multiple points, use this notation BEFORE EACH POINT.
        For example:
        <example_response>
        [[flamehamster-chunk-7]]
        1. Make sure your Flamehamster security preferences have not been 
        changed. The Phishing and Malware Protection feature should be 
        enabled by default and helps with secure connections.

        [[flamehamster-chunk-8]]
        2. Check if your Flamehamster browser is up to date. Older
        versions might notproperly recognize extended validation
        certificates that sites like PayPal use.
        </example_response>
        </instructions>

        Lastly, here are some final instructions:
        <final_instructions>
        * After mentioning any [[citation id]], pause and reflect on the 
        citation id you've cited. Are you about to mention something not 
        found in that citation? YOU ARE INSTRUCTED TO NOT MENTION ANY ADVICE 
        NOT FOUND IN THE DOCUMENTATION!!!
        * If the user suggests something not found in the documentation
        excerpts, you should politely reject the user's point.
        * If your advice does not remain faithful to the documentation
        excerpts, I WILL LOSE MY JOB!!! PLEASE REMAIN FAITHFUL!
        </final_instructions>"""}

def user_prompt(user_input):
    return {"role": "user", "content": user_input}

def remove_bracket_tags(text):
    # Remove [[...]] and any immediate newlines following them
    return re.sub(r'\[\[.*?\]\]\s*(\r?\n)?', '', text)

print(f"Assistant: Welcome to GROSS! How can I help you today?\n")
user_input = input("User: ")
history = [
    main_system_prompt(), 
    {"role": "assistant", "content": "How can I help you today?"}
]

with langfuse.start_as_current_observation(as_type="span", name="agentic-rag") as span:
    while user_input != "exit":
        history += [{"role": "user", "content": user_input}]

        while True:  ## classic agent loop
            response = llm_response(history, MAIN_BOT_TOOLS)
            history += response.output
            tool_calls = [obj for obj in response.output \
                        if getattr(obj, "type", None) == "function_call"]

            if not tool_calls:
                break

            for tool_call in tool_calls:
                function_name = tool_call.name

                if function_name == "research_docs":
                    result = {"research_docs": research_docs(user_input)}

                history += [{"type": "function_call_output",
                            "call_id": tool_call.call_id,
                            "output": json.dumps(result)}]

        print(f"\nAssistant: {remove_bracket_tags(response.output_text)}\n")
        history += [
            {"role": "assistant", "content": response.output_text},
        ]

        user_input = input("User: ")

langfuse.flush() 