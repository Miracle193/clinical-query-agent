from openai import OpenAI
import os
from prompts import build_prompt, SYSTEM_PROMPT
from dotenv import load_dotenv
load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

issues = {
        "subject": "SUB001",
        "field": "Age",
        "value": 250,
        "rule": "Expected age range 0-120",
        "severity": "High",
        "rule_id": "AGE001"
    }

def generate_query(issue):

    prompt = build_prompt(issue)

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {
                "role": "system",
                "content": SYSTEM_PROMPT
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.3
    )

    return response.choices[0].message.content

response = generate_query(issues)

print(response)