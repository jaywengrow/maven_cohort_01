from basic_llm import LLM

def translate_to_french(text):
    response = LLM().generate(
        string_prompt=f"Translate to French: {text}. "
    )
    return response["text"]

translation = translate_to_french("dragonfly")
print(translation)