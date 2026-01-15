import os
import json
from dotenv import load_dotenv
from langfuse.openai import openai
import yagmail

load_dotenv()
llm = openai

TOOLS = [                       # tool schema
    {
        "type": "function",
        "name": "send_email",
        "description": "Send an email containing a specific subject and body to a specific recipient.",
        "parameters": {
            "type": "object",
            "properties": {
                "recipient_email": { "type": "string" },
                "subject": { "type": "string" },
                "body": { "type": "string" },
            },
            "required": ["recipient_email", "subject", "body"],
        },
    }
]

def send_email(recipient_email, subject, body):
    yag = yagmail.SMTP(os.getenv("GMAIL_ACCOUNT"), oauth2_file="oauth.json")
    yag.send(to=recipient_email, subject=subject, contents=body)

def system_prompt():
    return """You are a friendly AI assistant who helps human users. In addition to your ability to converse with the user, you are equipped with the ability to send an email if the user so desires.

    Here's how to send an email. You first need to ensure that you have three pieces of information:

    1) The recipient email address
    2) The email subject
    3) The email body

    Then, when you're ready to send the email, use your send_email tool."""

assistant_message = "How can I help?"
user_input = input(f"\nAssistant: {assistant_message}\n\nUser: ")

history = [
    {"role": "developer", "content": system_prompt()},
    {"role": "assistant", "content": assistant_message},
    {"role": "user", "content": user_input}
]

while user_input != "exit":
    response = llm.responses.create(
        model="gpt-4.1-mini",
        input=history,
        tools=TOOLS     # include tool schema in LLM call
    )
    llm_response_text = response.output_text

    for item in response.output:
        if item.type == "function_call":
            print(item)                # uncomment to see OpenAI tool call
            function_call = item
            function_name = item.name
            args = json.loads(item.arguments)

            if function_name == "send_email":
                result = {"send_email": send_email(**args)}
                llm_response_text = "\nAssistant: I've sent your email! What else can I do to help?"

    print(llm_response_text)

    user_input = input("\nUser: ")
    history += [
        {"role": "assistant", "content": llm_response_text},
        {"role": "user", "content": user_input}
    ]

print("****HISTORY****")
print(history)