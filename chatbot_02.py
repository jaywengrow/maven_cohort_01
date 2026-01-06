from basic_llm import LLM

response = LLM().generate(
    string_prompt="What is the best food in the world?"
)

print(response["text"])