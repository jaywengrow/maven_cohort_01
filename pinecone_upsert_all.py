import os
from pathlib import Path
from dotenv import load_dotenv
from pinecone import Pinecone
import re

load_dotenv()

def split_markdown_by_h1(md_text):
    pattern = r"(?m)^# .+?(?=^# |\Z)"
    chunks = re.findall(pattern, md_text, re.DOTALL)
    return [chunk.strip() for chunk in chunks if chunk.strip()]

pc = Pinecone(api_key=os.getenv("PINECONE_API_KEY"))
dense_index = pc.Index("maven-gross") # replace 'maven-gross' with your own index name
data_dir = Path("data")

# Load and chunk all markdown files in the folder
for file_path in data_dir.glob("*.md"):
    records = []
    
    with open(file_path, "r", encoding="utf-8") as f:
        md_content = f.read()

    chunks = split_markdown_by_h1(md_content)
    manual_name = file_path.stem  # filename without extension (.md)

    for i, chunk in enumerate(chunks):
        print(f"{manual_name}-chunk-{i}",)
        records.append({
            "id": f"{manual_name}-chunk-{i}",  # must provide id explicitly
            "chunk_text": chunk, # this key (chunk_text) must match the "record field" in your Pinecone index's settings
            "manual": manual_name # custom metadata
        })

    dense_index.upsert_records("all-gross", records) # first argument is the "namespace" (https://docs.pinecone.io/guides/index-data/indexing-overview#namespaces)

print("Complete!")
