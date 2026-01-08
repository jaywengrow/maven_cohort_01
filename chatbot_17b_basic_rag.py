import os
from basic_llm import LLM
from pinecone import Pinecone

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

assistant_message = "Welcome to GROSS! How can I help?"
user_input = input(f"\nAssistant: {assistant_message}\n\nUser: ")

history = [
    {"role": "assistant", "content": assistant_message},
    {"role": "user", "content": user_input}
]

while user_input != "exit":
    documentation = search_docs(user_input) # RAG!
    response = LLM().generate(
        messages_prompt=history,
        system_prompt=f"""You are an AI customer support
            chatbot that represents a software company called GROSS, and you help
            GROSS customers with their software questions and problems.
            One GROSS product is a web browser called
            Flamehamster. You are to answer user queries solely on
            the following documentation: {documentation}""" 
    )

    llm_response_text = f"\nAssistant: {response["text"]}"
    print(llm_response_text)

    user_input = input("\nUser: ")
    history += [
        {"role": "assistant", "content": response["text"]},
        {"role": "user", "content": user_input}
    ]

print("\n\n****HISTORY****")
print(response["system_prompt"])
