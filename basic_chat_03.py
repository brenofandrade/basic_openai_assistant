from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
cliente = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

resposta = cliente.chat.completions.create(
    messages=[
        {
            "role":"system",
            "content" : """
            Classifique os produtos abaixo em uma das três categorias: 
            Higiene Pessoal, 
            Moda ou 
            Casa e dê uma descrição da categoria.
            """
        },
        {
            "role" : "user",
            "content" : """
            Escova de dentes de Banbu
            """
        }
    ],
    model="gpt-4",
    temperature=0,
    max_tokens=200,
    n=3
)


for contador in range(3):
    print(resposta.choices[contador].message.content)