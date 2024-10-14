import os
from openai import OpenAI 

MODEL = "gpt-4o-mini"
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

def prompt_gpt4(prompt):
    completion = client.chat.completions.create(
    model=MODEL,
    messages=[
        {"role": "user", "content": prompt}  
    ]
    )
    return completion.choices[0].message.content