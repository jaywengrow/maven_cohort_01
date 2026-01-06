from dotenv import load_dotenv
from openai import OpenAI

load_dotenv('.env')
llm = OpenAI()

response = llm.responses.create(
    model="gpt-4.1-mini",
    input="What is 7654 * 4567? Explain your reasoning step by step.",
    temperature=0
)

print(response.output_text)