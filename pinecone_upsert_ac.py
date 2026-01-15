import os
from dotenv import load_dotenv
from pinecone import Pinecone
import re

load_dotenv()

BATCH_SIZE = 96

def split_markdown_by_h1(md_text):
    # returns array of documentation text "chunks" - as separated by h1 tags
    pattern = r"(?m)^# .+?(?=^# |\Z)"
    chunks = re.findall(pattern, md_text, re.DOTALL)
    return [chunk.strip() for chunk in chunks if chunk.strip()]


with open("activecampaign-ai.md", "r", encoding="utf-8") as f:
    md_content = f.read()

chunks = split_markdown_by_h1(md_content)

records = []
for i, chunk in enumerate(chunks):
    records.append({
        "id": f"chunk-{i}",        # must provide id explicitly
        "chunk_text": chunk,       # must match the record field in the index
    })

pinecone = Pinecone(api_key=os.getenv("PINECONE_API_KEY"))
dense_index = pinecone.Index("ac")  # replace with your index name

# 🔁 Upsert in batches of 96
for i in range(0, len(records), BATCH_SIZE):
    print(i)
    batch = records[i : i + BATCH_SIZE]
    dense_index.upsert_records(
        namespace="ac",
        records=batch,
    )
    print(f"Upserted records {i}–{i + len(batch) - 1}")
