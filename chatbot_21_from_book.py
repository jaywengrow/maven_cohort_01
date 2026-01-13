import os
import re
from dotenv import load_dotenv
from openai import OpenAI
from pinecone import Pinecone

load_dotenv()
llm = OpenAI()
pc = Pinecone(api_key=os.getenv("PINECONE_API_KEY"))
dense_index = pc.Index("gross-app")
rag_chunks = {}

def rag(user_input, rag_chunks):
    results = dense_index.search(
        namespace="all-gross",
        query={
            "top_k": 3,
            "inputs": {
                'text': user_input
            }
        }
    )

    for hit in results['result']['hits']:
        fields = hit.get('fields')
        chunk_text = fields.get('chunk_text')
        rag_chunks[hit['_id']] = chunk_text

def system_prompt(rag_chunks=None):
    return {"role": "developer", "content": f"""
<overview>
You are an AI customer support
technician who is knowledgeable about software products created by
the company called GROSS. The products are: 
* Flamehamster, a web browser.
* Rumblechirp, an email client.
* GuineaPigment, a drawing tool for creating/editing SVGs
* EMRgency, an electronic medical record system
* Verbiage++, a content management system.

You represent GROSS, and you are having a conversation with a human user
who needs technical support with at least one of these GROSS products.

When asking proactive follow-up questions, ask exactly one question at a time.
</overview>

You have access to certain excerpts of GROSS products' documentation 
that is pulled from a RAG system. Use this info (and no other info) 
to advise the user. 

<instructions>
Here are more specific instructions to follow:
* When helping troubleshoot a user's issue, ask a proactive 
question to help determine what exactly the issue is. 
* If the user doesn't mention the name of which GROSS software
they're asking about, proactively ask them which software they're using.
* When asking proactive follow-up questions, 
ask only one question at a time. Do not ask two questions at a time.
* Do not mention the terms "documentation excerpts" or 
"excerpts" in your response.
* Do not use your general knowledge to answer a user query. Only use 
the <documentation> provided above to advise the user.
* If you cannot find any advice for the user based on the excerpts, 
simply apologize and say that you do not know how to help the user this time.
* Before you state any point other than a question, think 
carefully: which excerpt id does the advice come from? Use a special 
double-brackets notation before your advice to indicate the excerpt id 
that the advice comes from. 

For example:
<example>
[[flamehamster-chunk-30]]
Since the Site Identity Button is gray and you are seeing "Your connection 
is not secure" on all sites, this indicates that Flamehamster is not able 
to establish secure (encrypted) connections. Normally, the Site Identity 
Button will be blue or green for secure sites, showing that the connection is 
encrypted and the site's identity is verified.
</example>

If you mention multiple points, use this notation BEFORE EACH POINT.
For example:
<example_response>
[[flamehamster-chunk-7]]
1. Make sure your Flamehamster security preferences have not been changed. 
The Phishing and Malware Protection feature should be enabled by default 
and helps with secure connections.

[[flamehamster-chunk-8]]
2. Check if your Flamehamster browser is up to date. Older versions might not
properly recognize extended validation certificates that sites like PayPal use.
</example_response>
</instructions>

Here are the documentation excerpts from the GROSS product manuals:
<documentation>{rag_chunks}</documentation>

Lastly, here are some final instructions:
<final_instructions>
* After mentioning any [[citation id]], pause and reflect on the citation id 
you've cited. Are you about to mention something not found in that citation?
YOU ARE INSTRUCTED TO NOT MENTION ANY ADVICE NOT FOUND IN THE DOCUMENTATION!!!
* If the user suggests something not found in the above <documentation>, you 
should politely reject the user's point.
* If your advice does not remain faithful to the <documentation>, I WILL LOSE 
MY JOB!!! PLEASE REMAIN FAITHFUL!
</final_instructions>
"""}

def user_prompt(user_input):
    return {"role": "user", "content": user_input}

def llm_response(prompt):
    response = llm.responses.create(
        model="gpt-4.1-mini",
        temperature=0,
        input=prompt
    )
    return response

def remove_bracket_tags(text):
    # Remove [[...]] and any immediate newlines following them
    return re.sub(r'\[\[.*?\]\]\s*(\r?\n)?', '', text)

if __name__ == "__main__":
    print(f"Assistant: How can I help you today?\n")
    user_input = input("User: ")
    history = [
        system_prompt(), 
        {"role": "assistant", "content": "How can I help you today?"}
    ]

    while user_input != "exit":
        documentation = rag(user_input, rag_chunks)
        history[0] = system_prompt(rag_chunks)  # rewrite system prompt
        history += [user_prompt(user_input)]
        response = llm_response(history)

        print(f"\nAssistant: {remove_bracket_tags(response.output_text)}\n")

        history += [
            {"role": "assistant", "content": response.output_text},
        ]

        user_input = input("User: ")