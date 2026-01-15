from dotenv import load_dotenv
from openai import OpenAI
import csv
from pydantic import BaseModel

load_dotenv('.env')
llm = OpenAI()

def eval_assumed_product(trace):
    class Judgment(BaseModel):
        reasoning: str
        judgment: str

    response = llm.responses.parse(
        model="gpt-4.1",
        temperature=0,
        text_format=Judgment,
        input=f"""<overview>You are an LLM judge that evaluates the output of another LLM called the "troubleshooter". The troubleshooter is a chatbot assistant that advises human users about
        software from a company called GROSS. The products are: 
            * Flamehamster, a web browser.
            * Rumblechirp, an email client.
            * GuineaPigment, a drawing tool for creating/editing SVGs
            * EMRgency, an electronic medical record system
            * Verbiage++, a content management system.
        The troubleshooter helps troubleshoot user issues with these software products.
        Now, sometimes, it may not be clear from the user input which product they're
        discussing. When this happens, the chatbot should ask a clarifying question to
        help figure out which product the user is referring to.</overview>

        <instructions>
        You are to inspect a conversation between the troubleshooter LLM and the human
        user and output a judgment of either "PASS" or "FAIL"
        First, though, you should separately output your reasoning. Then, output either PASS or FAIL based on your judgment. Your output will be a JSON object such as:
        {{reasoning: 'your reasoning goes here', judgment: 'FAIL'}} or 
        {{reasoning: 'your reasoning goes here', judgment: 'PASS'}}
        
        * Render FAIL if the troubleshooter gives advice
        before the user explicitly mentions which product the user is discussing.
        * Render PASS otherwise.
        </instructions>

        Here are some examples:
        <examples>
        <example>
        User: the app is crashing
        Assistant: Which GROSS app is crashing? Please choose one: Flamehamster (browser), Rumblechirp (email), GuineaPigment (SVG editor), EMRgency (EMR), or Verbiage++ (CMS).
        User: Verbiage
        Assistant: Verbiage++ can crash sometimes if...

        This should be a PASS, since the troubleshooter assistant only gave advice
        once the user was clearly discussing the Verbiage++ product.
        </example>

        <example>
        User: how do I download your software?
        Assistant: To download Verbiage++, you'll need to visit the website...

        This should be FAIL since the assistant is giving advice before clarifying
        which software the user is talking about.
        </example>

        <example>
        User: how do I download Verbiage?
        Assistant: To download Verbiage++, visit the website...

        This is a PASS, since the user mentioned the product name before the assistant gave advice. This is so even though the precise name is "Verbiage++" and the
        user mentioned just "Verbiage".
        </example>

        <example>
        User: how do I download rmblechip?
        Assistant: To download Rumblechirp, visit the website...

        This is a PASS, since before the assistant gives advice, it's already clear that the user is referring to Rumblechirp. Although the user's input contained
        typos in the product name, it's still very clear that they're referring
        to Rumblechirp.
        </example>

        <example>
        User: how do I download the SVG drawing tool?
        Assistant: To download GuineaPigment, visit the website...

        This is a FAIL, since although it's highly likely that the user is referring
        to GuineaPigment, the only SVG editor among GROSS products, we still require
        that the user specify the product name before the assistant gives advice.
        </example>
        </examples>

        Now, it's your turn. Here is a conversation; determine whether it's PASS or FAIL:

        {trace}
        """
    )

    data = response.output_parsed
    return data.judgment, data.reasoning

def run_evals(traces_file):
    fails = []
    num_passes = 0
    trace_number = 0

    with open(traces_file, encoding="utf-8") as f:
        for line in f:
            trace = line.strip()
            llm_judgment, reasoning = eval_assumed_product(trace)

            trace_number += 1
            if llm_judgment == "PASS":
                print(f"{trace_number}: PASS")
                num_passes += 1
            else:
                print(f"{trace_number}: FAIL")
                fails.append({"trace_number": trace_number, "trace": trace, "reasoning": reasoning})

    print(fails)
    
    accuracy = num_passes / trace_number if trace_number else 0.0
    print(f"Traces: {trace_number}")
    print(f"Passes: {num_passes}")
    print(f"Fails: {len(fails)}")
    print(f"Accuracy: {accuracy:.2f}%")


run_evals("production_traces.csv")