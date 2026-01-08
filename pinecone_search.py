import os
from dotenv import load_dotenv
from pinecone import Pinecone

load_dotenv()
pc = Pinecone(api_key=os.getenv("PINECONE_API_KEY"))
dense_index = pc.Index("maven-gross")

query = "how can I remove a bookmark?"

# Retrieve relevant chunks from vector DB:
results = dense_index.search(
   namespace="all-gross",
   query={
       "top_k": 3,
       "inputs": {
           'text': query
       }
   }
)

# print(results)

# Convert chunks into one long string of documentation
documentation = ""
for hit in results['result']['hits']:
   fields = hit.get('fields')
   chunk_text = fields.get('chunk_text')
   documentation += chunk_text

print(documentation)
