from dotenv import load_dotenv
from openai import OpenAI

load_dotenv('.env')
llm = OpenAI()

response = llm.responses.create(
    model="gpt-4.1-nano",
    input="Which celebrity was born with eleven fingers?",
    temperature=0,
    max_output_tokens=100
)

print(response.output_text)