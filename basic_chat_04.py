import os
from openai import OpenAI
from dotenv import load_dotenv
load_dotenv(override=True)

key = os.getenv("OPENAI_API_KEY")

if key == "":
    raise ValueError("Nenhuma chave encontrada! Por favor, crie uma chave.")

# Initiate the conection
client = OpenAI(api_key=key)


def categoriza_produto(nome_produto, lista_categorias):
    
    
    model = "gpt-4"
    temperature = 0
    max_tokens=200

    prompt_system = f"""
    Você é um categorizador de produtos.
    Você deve assumir as categorias presentes na lista abaixo.

    # Lista de Categorias Válidas: \n{'\t\n'.join(f'- {categoria}' for categoria in lista_categorias.split(","))}

    # Formato da Saída
    Produto: Nome do Produto
    Categoria: apresente a categoria do produto

    # Exemplo de Saída
    Produto: Escova elétrica com recarga solar
    Categoria: Eletrônicos"""

    
    resposta = client.chat.completions.create(
        messages=[
            {
                "role":"system",
                "content" : prompt_system
            },
            {
                "role" : "user",
                "content" : nome_produto
            }
        ],
        model=model,
        temperature=temperature,
        max_tokens=max_tokens
    )

    return resposta.choices[0].message.content


categorias_validas = input("Informe as categorias válidas, separadas por vírgula: ")

while True:

    nome_produto = input("Digite o nome do produto ou sair para encerrar: ")
    
    if nome_produto.lower() in ['sair', 'quit', 'bye']:
        print("Valeu!!!")
        break
    
    texto_resposta = categoriza_produto(nome_produto, categorias_validas)

    print(texto_resposta)