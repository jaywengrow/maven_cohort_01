from basic_llm import LLM

user_input = input("Assistant: How can I help you today?\n\nUser: ")

while user_input != "exit":
    response = LLM().generate(
        string_prompt=user_input
    )

    print(f"\nAssistant: {response["text"]}")

    user_input = input("\nUser: ")
