from basic_llm import LLM

def translate_to_french(text):
    response = LLM().generate(
        string_prompt=f"Translate the following into French, and only include the translation itself with no extra introductory text: {text}"
    )
    return response["text"]

translation = translate_to_french("dragonfly")
print(translation)