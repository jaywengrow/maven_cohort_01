from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
llm = OpenAI()

response = llm.responses.create(
    model="gpt-4.1-nano",
    input="Who was the first US president?"
)

print(response.output_text)