from dotenv import load_dotenv
import os
from langfuse.openai import openai
from pinecone import Pinecone

load_dotenv('.env')
llm = openai
pc = Pinecone(api_key=os.getenv("PINECONE_API_KEY"))
dense_index = pc.Index("maven-gross")

def search_docs(query):
    results = dense_index.search(
        namespace="all-gross",
        query={
            "top_k": 3,
            "inputs": {
                'text': query
            }
        }
    )

    documentation = ""
    for hit in results['result']['hits']:
        fields = hit.get('fields')
        chunk_text = fields.get('chunk_text')
        documentation += chunk_text

    return documentation

def system_prompt(documentation):
    return f"""You are an AI customer support
            technician who is knowledgeable about software products created by
            the company called GROSS. The products are: 
            * Flamehamster, a web browser.
            * Rumblechirp, an email client.
            * GuineaPigment, a drawing tool for creating/editing SVGs
            * EMRgency, an electronic medical record system
            * Verbiage++, a content management system.

            You are to answer user queries solely on
            the following documentation: {documentation}.
            
            Be sure to make sure the user mentions the specific GROSS
            product before giving advice.
            
            Also, don't rush headlong into giving advice without first
            proactively asking clarifying questions to help troubleshoot
            the user's issue. Only ask one clarifying question at a time.""" 

# Main conversation loop:
assistant_message = "Welcome to GROSS! How can I help?"
user_input = input(f"\nAssistant: {assistant_message}\n\nUser: ")

history = [
    {"role": "developer", "content": ""},
    {"role": "assistant", "content": assistant_message},
    {"role": "user", "content": user_input}
]

while user_input != "exit":
    documentation = search_docs(user_input)
    history[0] = {"role": "developer", "content": system_prompt(documentation)}

    response = llm.responses.create(
        model="gpt-4.1",  # stronger model
        input=history,
        temperature=0
    )

    llm_response_text = f"\nAssistant: {response.output_text}"
    print(llm_response_text)

    user_input = input("\nUser: ")
    history += [
        {"role": "assistant", "content": response.output_text},
        {"role": "user", "content": user_input}
    ]

print("****HISTORY****")
print(history)