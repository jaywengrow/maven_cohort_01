from dotenv import load_dotenv
from openai import OpenAI
import anthropic

load_dotenv('.env')
PROVIDER = "claude"
# PROVIDER = "openai"

class LLM:
    def generate(
        self,
        string_prompt=None,
        messages_prompt=None,
        system_prompt=None,
        temperature=0,
        max_tokens=512,
        tools=None,
    ):
        if PROVIDER == "openai":
            
            llm = OpenAI()
            if string_prompt:
                prompt = string_prompt
            else:
                prompt = messages_prompt
                if system_prompt:
                    prompt.insert(0, {"role": "developer", "content": system_prompt})
                else: 
                    prompt = messages_prompt
            response = llm.responses.create(
                model="gpt-4.1-mini",
                input=prompt,
                temperature=temperature,
                max_output_tokens=max_tokens,
                tools=tools
            )

            response_data = response
            response_text = response.output_text
        
        elif PROVIDER == "claude":

            if string_prompt:
                prompt = [
                    {
                        "role": "user",
                        "content": string_prompt
                    }
                ]
            else:
                prompt = messages_prompt

            llm = anthropic.Anthropic()

            response = llm.messages.create(
                model="claude-haiku-4-5-20251001",
                max_tokens=max_tokens,
                temperature=temperature,
                messages=prompt,
                **({"system": system_prompt} if system_prompt is not None else {})
            )

            response_data = response
            response_text = response.content[0].text

        return {
            "metadata": response_data,
            "text": response_text, 
            "system_prompt": system_prompt
            }
