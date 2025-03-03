"""
repetições
while(enquanto)
Executa uma ação enquanto uma condição for verdadeira
loop infinito -> Quando um código não tem fim
"""

condicao = True

while condicao:
    nome = input("Qual seu nome? ")
    print(f"O seu nome é {nome}")

    if nome == 'sair':
        break

print("Acabou")