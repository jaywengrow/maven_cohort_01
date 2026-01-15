from dotenv import load_dotenv
import anthropic

load_dotenv('.env')
llm = anthropic.Anthropic()

message = llm.messages.create(
    model="claude-sonnet-4-5",
    max_tokens=1000,
    messages=[
        {
            "role": "user",
            "content": "Who was the first US president?"
        }
    ]
)
print(message.content[0].text)