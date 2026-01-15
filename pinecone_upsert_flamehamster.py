import os
from dotenv import load_dotenv
from pinecone import Pinecone
import re

load_dotenv()

def split_markdown_by_h1(md_text): # returns array of documentation text "chunks" - as separated by h1 tags
    pattern = r"(?m)^# .+?(?=^# |\Z)"
    chunks = re.findall(pattern, md_text, re.DOTALL)
    return [chunk.strip() for chunk in chunks if chunk.strip()]


with open("data/flamehamster.md", "r", encoding="utf-8") as f:
    md_content = f.read()

chunks = split_markdown_by_h1(md_content)
records = []  # our data in a special format that Pinecone expects 

for i in range(len(chunks)):
    print(i)
    records.append({
        "id": f"chunk-{i}",      # must provide id explicitly
        "chunk_text": chunks[i], # this key (chunk_text) must match the "record field" in your Pinecone index's settings
        "manual": "flamehamster" # custom metadata
        })


pinecone = Pinecone(api_key=os.getenv("PINECONE_API_KEY"))
dense_index = pinecone.Index("maven-gross") # replace 'maven-gross' with your own index name
dense_index.upsert_records("flamehamster", records) # first argument is the "namespace" (similar to metadata, but a different construct)
