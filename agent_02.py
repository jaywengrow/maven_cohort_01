import os
from dotenv import load_dotenv
from openai import OpenAI
import yagmail 

load_dotenv()
llm = OpenAI()

def send_email(body):
    yag = yagmail.SMTP(os.getenv("GMAIL_ACCOUNT"), oauth2_file="oauth.json")
    yag.send(to="jay@commonsensedev.com", subject="Test email", contents=body)

def system_prompt():
    return """You are a friendly AI assistant who helps human users. In addition to your ability to converse with the user, you are equipped with the ability to send an email if the user so desires. The email subject and recipient is fixed; the user can only provide
    the body of the email. DO NOT ask the user for the email subject or who to send the 
    email to.

    Here's how to send an email. You first need to ensure that the user provides the body of what should be sent in the email.

    Then, when you're ready to send the email, output the following precise syntax:

    [[email body]]

    For example, if the user wants to email the message "Hey, what's up?", output:

    [[Hey, what's up?]]"""

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
    )

    llm_response_text = f"\nAssistant: {response.output_text}"
    print(llm_response_text)

    user_input = input("\nUser: ")
    history += [
        {"role": "assistant", "content": response.output_text},
        {"role": "user", "content": user_input}
    ]
