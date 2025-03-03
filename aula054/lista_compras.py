"""
Faça uma lista de comprar com listas
O usuário deve ter a possibilidade de
inserir, apagar e listar valores da sua lista
Não permita que o programa quebre com 
erros de índices inexistentes na lista.
"""

import os

lista_de_compras = []

valores_permitidos_funcao = 'ials'

while True:
    print(f"{'ESCOLHA UMA OPÇÃO':*^50}")
    funcao = input("[I]nserir, [A]pagar,[L]istar, [S]air: " ).lower()

    if funcao not in valores_permitidos_funcao:
        os.system('cls' or 'clear')
        print(f"Valor não é válido! Escolha I,A ou L. ")
        continue

    if funcao == 'i':
        os.system('cls' or 'clear')
        valor_inserir = input("Oque deseja adicionar na lista? ").lower()

        if not valor_inserir:
            print(f"Valor vazio escolha a opção novamente! ")
            continue

        lista_de_compras.append(valor_inserir)


    if funcao == 'a':
        os.system('cls' or 'clear')
        valor_apagar = input("Oque deseja apagar da lista? ")

        if not valor_apagar:
            print(f"Valor vazio escolha a opção novamente! ")
            continue

        int_valor_apagar = int(valor_apagar)

        try:
            valor_excluido = lista_de_compras.pop(int_valor_apagar)
            print(f"Valor {valor_excluido} foi excluído com sucesso! ")
        except:
            print(f"Indice não encontrado!")
            continue

    if funcao == 'l':
        os.system('cls' or 'clear')
        if len(lista_de_compras) == 0:
            print("Lista vazia!")
            continue     

        for indice,valor in enumerate(lista_de_compras):
            print(f"Id: {indice} --> valor: {valor}")
        continue

    if funcao == 's':
        break