import openai

openai.api_key = "<<YOUR API KEY"  

def gerar_desafio(topicos):
    import random
    topico = random.choice(topicos)
    prompt = f"Crie um desafio simples de programação em Python sobre o tópico: {topico}"
    resposta = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    return resposta.choices[0].message.content.strip()


def corrigir_codigo(enunciado, codigo_usuario):
    prompt = f"""Aqui está o enunciado do desafio:
{enunciado}

E aqui está a solução do aluno:
{codigo_usuario}

Corrija a solução, aponte melhorias e sugira como o código pode ser otimizado."""
    resposta = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    return resposta.choices[0].message.content.strip()

