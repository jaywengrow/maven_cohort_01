from basic_llm import LLM

assistant_message = "How can I help?"
user_input = input(f"\nAssistant: {assistant_message}\n\nUser: ")

history = [
    {"role": "assistant", "content": assistant_message},
    {"role": "user", "content": user_input}
]

while user_input != "exit":
    response = LLM().generate(
        messages_prompt=history,
        system_prompt="You are a chatbot that talks like a pirate."
    )

    llm_response_text = f"\nAssistant: {response["text"]}"
    print(llm_response_text)

    user_input = input("\nUser: ")
    history += [
        {"role": "assistant", "content": response["text"]},
        {"role": "user", "content": user_input}
    ]
