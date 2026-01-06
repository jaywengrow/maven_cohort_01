from basic_llm import LLM

user_input = input("Ask away!\n")

response = LLM().generate(
    string_prompt=f"Respond like a pirate to this query: {user_input}"
)

print(response["text"])