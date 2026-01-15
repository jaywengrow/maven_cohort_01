import os
import re
from dotenv import load_dotenv
from openai import OpenAI
import yagmail  # email-sending library

load_dotenv()
llm = OpenAI()

def send_email(body):
    yag = yagmail.SMTP(os.getenv("GMAIL_ACCOUNT"), oauth2_file="oauth.json")
    yag.send(to="jay@commonsensedev.com", subject="Test email", contents=body)

def extract_double_brace(text):  # function that extracts data from [[ ]]
    """
    Extracts and returns the text inside the first [[...]] occurrence.
    Returns None if no match is found.
    """
    match = re.search(r"\[\[(.*?)\]\]", text)
    return match.group(1) if match else None

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

    email_body = extract_double_brace(response.output_text) # check for tool use
    if email_body:   # if tool is called
        send_email(email_body)
        llm_response_text = "\nAssistant: I've sent your email! What else can I do to help?"
    else:
        llm_response_text = f"\nAssistant: {response.output_text}"

    print(llm_response_text)

    user_input = input("\nUser: ")
    history += [
        {"role": "assistant", "content": response.output_text},
        {"role": "user", "content": user_input}
    ]
