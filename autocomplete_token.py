from dotenv import load_dotenv
from openai import OpenAI
import sys
import tiktoken

load_dotenv('.env')
llm_client = OpenAI()

def tokenize_text(text, model="gpt-4o"):
    enc = tiktoken.encoding_for_model(model)
    token_ids = enc.encode(text)
    tokens = [enc.decode([tid]) for tid in token_ids]
    return tokens

response = llm_client.responses.create(
    model="gpt-4.1-mini",
    input=f"""<instructions>
    I will give you the beginning of a sentence (one or two words),
    and you will complete the sentence. Your output should consist of the
    entire sentence from the beginning.</instructions
    <example>For example, if I start off the sentence
    with 'Today', you might output 'Today, I think I'll ride a bike.'</example>
    
    Here is the beginning of the sentence you are to complete: 
    
    {sys.argv[1]}"""
)

tokens = tokenize_text(response.output_text)

for token in tokens:
    input()
    print(token.strip(), end=" ", flush=True)