import random
import os


perguntas = [
    {
        "pergunta": "Quanto é 5+3?",
        "opcoes": ["7", "8", "9", "10"],
        "resposta": "8",
        "pos_resposta":"1"
    },
    {
        "pergunta": "Qual é a capital da França?",
        "opcoes": ["Madrid", "Paris", "Londres", "Berlim"],
        "resposta": "Paris",
        "pos_resposta":"1"
    },
    {
        "pergunta": "Quantos lados tem um triângulo?",
        "opcoes": ["2", "3", "4", "5"],
        "resposta": "3",
        "pos_resposta":"1"
    },
    {
        "pergunta": "Qual é o resultado de 9 x 6?",
        "opcoes": ["42", "54", "48", "56"],
        "resposta": "54",
        "pos_resposta":"1"
    },
    {
        "pergunta": "Qual destes é um mamífero?",
        "opcoes": ["Cobra", "Tubarão", "Golfinho", "Papagaio"],
        "resposta": "Golfinho",
        "pos_resposta":"2"
    },
    {
        "pergunta": "Qual é o maior planeta do sistema solar?",
        "opcoes": ["Terra", "Marte", "Júpiter", "Vênus"],
        "resposta": "Júpiter",
        "pos_resposta":"2"
    },
    {
        "pergunta": "Quem escreveu 'Dom Quixote'?",
        "opcoes": ["Machado de Assis", "Miguel de Cervantes", "William Shakespeare", "José Saramago"],
        "resposta": "Miguel de Cervantes",
        "pos_resposta":"1"
    },
    {
        "pergunta": "Quanto é 12 dividido por 4?",
        "opcoes": ["2", "3", "4", "6"],
        "resposta": "3",
        "pos_resposta":"1"
    },
    {
        "pergunta": "Qual destes animais bota ovos?",
        "opcoes": ["Gato", "Cachorro", "Ornitorrinco", "Leão"],
        "resposta": "Ornitorrinco",
        "pos_resposta":"2"
    },
    {
        "pergunta": "Qual o nome do gás essencial para a respiração humana?",
        "opcoes": ["Hidrogênio", "Oxigênio", "Nitrogênio", "Gás Carbônico"],
        "resposta": "Oxigênio",
        "pos_resposta":"1"
    }
]

def opcoes(opcoes):
    for chave, valor in enumerate(opcoes):
        print(f"{chave} --> {valor}")

def valida_valor(valor):
    valores_validos = '0123'
    if valor not in valores_validos: 
        return False
    return True

def verifica_pergunta(pergunta):
    os.system('cls' or 'clear')
    print(pergunta['pergunta'])
    opcoes(pergunta['opcoes'])
   
    resposta = input("Digite a opção correta: ")
    
    if not valida_valor(resposta):
        return 'erro'

    if resposta == pergunta['pos_resposta']:
        return True
    return False

def testa_acerto(perguntas):
    qtd_perguntas = len(perguntas)
    pergunta_sorteada = random.randint(0,qtd_perguntas - 1)

    resultado = verifica_pergunta(perguntas[pergunta_sorteada])
    if resultado == 'erro':
        return 'erro'

    if resultado:
        print(f"Resposta correta: {perguntas[pergunta_sorteada]['resposta']}")
        return True

    print(
        f"Resposta incorreta!",f'Resposta correta era {perguntas[pergunta_sorteada]['pos_resposta']} -->',
        f"{perguntas[pergunta_sorteada]['resposta']}"
    )
    return False
    
    
contador_acertos = 0
contador_erros = 0

while True:
    resultado = testa_acerto(perguntas)
    if resultado is True:
        contador_acertos += 1
    elif not resultado:
        contador_erros += 1
    else:
        print("Opção inválida !")
        input()
        continue

    continuar = input("Continuar [S]im ou [N]ão ? ").lower()
    
    if continuar == 'n':
        print(f"Total de acerto {contador_acertos}")
        print(f"Total de erros {contador_erros}")
        break