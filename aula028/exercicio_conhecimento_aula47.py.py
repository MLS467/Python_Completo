"""
Exercício
Peça ao usuário para digitar seu nome
Peça ao usuário para digitar sua idade
Se nome e idade forem digitados:
    Exiba:
        Seu nome é {nome}
        Seu nome invertido é {nome invertido}
        Seu nome contém (ou não) espaços
        Seu nome tem {n} letras
        A primeira letra do seu nome é {letra}
        A última letra do seu nome é {letra}
Se nada for digitado em nome ou idade: 
    exiba "Desculpe, você deixou campos vazios."

"""

nome = input("Digite seu nome ")
idade = input("Digite sua idade ")

if not nome or not idade:
    print("Desculpe, você deixou campos vazios.")
else:
    if ' ' in nome:
        contem = "contém"
    else:
        contem = "não contém"

    print(
        f"Seu nome é {nome}",
        f"Seu nome invertido é {nome[::-1]}",
        f"Seu nome contém {len(nome)} letras",
        f"Seu nome {contem} espaços",
        f"A primeira letra do seu nome é {nome[0]}",
        f"A última letra do seu nome é {nome[-1]}",
        sep="\n"
        )