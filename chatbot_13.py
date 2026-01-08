from basic_llm import LLM

intro = "Below is an endless conversation between a pirate AI assistant and a human user:"
assistant_message = "Assistant: Ahoy! How can I help you today?\n\nUser: "
user_input = input(assistant_message)
history = intro + assistant_message + user_input

while user_input != "exit":
    response = LLM().generate(
        string_prompt=history
    )

    llm_response_text = f"\nAssistant: {response["text"]}"
    print(llm_response_text)

    user_input = input("\nUser: ")
    history += f"{llm_response_text}\n\nUser: {user_input}\n"
