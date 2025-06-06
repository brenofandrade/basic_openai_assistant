import os
from openai import OpenAI

from dotenv import load_dotenv
load_dotenv(override=True)

key = os.getenv("OPENAI_API_KEY")

if key == "":
    raise ValueError("Nenhuma chave encontrada! Por favor, crie uma chave.")

# Read the instructions
with open('instructions/instruction_01.txt', 'r') as file:
    instructions = file.read()

# Initiate the conection
client = OpenAI(api_key=key)

# Send the request
completion = client.chat.completions.create(
    model='gpt-4o',
    messages=[
        {
            "role": "user",
            "content": instructions
        }
    ]
)

# Show the response
print(completion.choices[0].message.content)
