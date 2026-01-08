from basic_llm import LLM

assistant_message = "Assistant: How can I help you today?\n\nUser: "
user_input = input(assistant_message)
history = assistant_message + user_input

while user_input != "exit":
    response = LLM().generate(
        string_prompt=user_input
    )

    print(f"\nAssistant: {response["text"]}")

    user_input = input("\nUser: ")
