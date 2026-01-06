from basic_llm import LLM

user_input = input("I'm a chatbot! Ask me anything:\n")

response = LLM().generate(
    string_prompt=user_input
)

print(response["text"])