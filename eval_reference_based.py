from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
llm = OpenAI()


def classify_manual(conversation):
    response = llm.responses.create(
        model="gpt-4.1-nano",
        temperature=0,
        input=f"""Classify which software product the user is referring to in 
        their final prompt of the following conversation. Your output should
        be limited to one of the following choices: [flamehamster, 
        rumblechirp, verbiage++, guineapigment, emrgency, unsure]. The option
        of unsure should be used only if you're not certain which software 
        the user is referring to. Here is the conversation: {conversation}"""
    )
    return response.output_text


def eval_classify_manual():
    conversation = "help me install Verbiage"
    if classify_manual(conversation) == "verbiage++":
        return "PASS"
    else: 
        return "FAIL"

print(eval_classify_manual())
