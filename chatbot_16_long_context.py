from basic_llm import LLM

with open("data/flamehamster.md", "r", encoding="utf-8") as file: # obtain proprietary docs
   documentation = file.read()

assistant_message = "Welcome to GROSS! How can I help?" # new intro message
user_input = input(f"\nAssistant: {assistant_message}\n\nUser: ")

history = [
    {"role": "assistant", "content": assistant_message},
    {"role": "user", "content": user_input}
]

while user_input != "exit":
    response = LLM().generate(
        messages_prompt=history,
        system_prompt=f"""You are an AI customer support
            chatbot that represents a software company called GROSS, and you help
            GROSS customers with their software questions and problems.
            One GROSS product is a web browser called
            Flamehamster. You are to answer user queries solely on
            the following documentation: {documentation}"""  # new system prompt
    )

    llm_response_text = f"\nAssistant: {response["text"]}"
    print(llm_response_text)

    user_input = input("\nUser: ")
    history += [
        {"role": "assistant", "content": response["text"]},
        {"role": "user", "content": user_input}
    ]

print("\n\n****HISTORY****")
print(history)
