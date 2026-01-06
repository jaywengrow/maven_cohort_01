from dotenv import load_dotenv
from openai import OpenAI
import sys

load_dotenv('.env')
llm_client = OpenAI()

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

words = response.output_text.split()

for word in words:
    input()
    print(word, end=" ", flush=True)