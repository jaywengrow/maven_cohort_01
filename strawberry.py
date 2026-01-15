from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
llm = OpenAI()

response = llm.responses.create(
    model="gpt-4.1-nano",
    input="How many letter 'r' are in there in the word 'strawberry'?"
)

print(response.output_text)