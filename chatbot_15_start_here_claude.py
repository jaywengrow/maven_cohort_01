from dotenv import load_dotenv
import anthropic

load_dotenv('.env')
llm = anthropic.Anthropic()

assistant_message = "How can I help?"
user_input = input(f"\nAssistant: {assistant_message}\n\nUser: ")

history = [
    {"role": "assistant", "content": assistant_message},
    {"role": "user", "content": user_input}
]

while user_input != "exit":
    response = llm.messages.create(
        model="claude-haiku-4-5-20251001",
        temperature=0,
        max_tokens=1000,
        system="You are a chatbot that talks like a pirate.",
        messages=history,
    )

    llm_response_text = f"\nAssistant: {response.content[0].text}"
    print(llm_response_text)

    user_input = input("\nUser: ")
    history += [
        {"role": "assistant", "content": response.content[0].text},
        {"role": "user", "content": user_input}
    ]
