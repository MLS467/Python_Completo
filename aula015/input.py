# nome = input('Qual seu nome ')

# print(f"seu nome é {nome=}")
def transforma_int(x):
    return int(x)

numero = 1
while transforma_int(numero) > 0:
    numero = input("Digite um número: ")
    numero2 = input("Digite outro número: ")
    
    if numero.isnumeric() and numero2.isnumeric():
        print(transforma_int(numero)+transforma_int(numero2))
    else:
        print(f"Valor inválido")
    
