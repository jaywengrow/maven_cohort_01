import os
from dotenv import load_dotenv
from openai import OpenAI
import yagmail  # email-sending library

load_dotenv()
llm = OpenAI()

def send_email(body):  # a function that sends an email
    yag = yagmail.SMTP(os.getenv("GMAIL_ACCOUNT"), oauth2_file="oauth.json")
    yag.send(to="jay@commonsensedev.com", subject="Test email", contents=body)

send_email("this is a test")

assistant_message = "How can I help?"
user_input = input(f"\nAssistant: {assistant_message}\n\nUser: ")

history = [
    {"role": "developer", "content": "You are a helpful chatbot."},
    {"role": "assistant", "content": assistant_message},
    {"role": "user", "content": user_input}
]

while user_input != "exit":
    response = llm.responses.create(
        model="gpt-4.1-mini",
        input=history,
    )

    llm_response_text = f"\nAssistant: {response.output_text}"
    print(llm_response_text)

    user_input = input("\nUser: ")
    history += [
        {"role": "assistant", "content": response.output_text},
        {"role": "user", "content": user_input}
    ]
