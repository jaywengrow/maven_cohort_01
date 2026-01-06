from dotenv import load_dotenv
from openai import OpenAI

load_dotenv('.env')
llm = OpenAI()

response = llm.responses.create(
    model="gpt-4.1-nano",
    input="Who is the current US president?",
    temperature=0
)

print(response.output_text)