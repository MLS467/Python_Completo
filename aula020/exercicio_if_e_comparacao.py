primeiro_valor = input("Digite o primeiro valor: ")

segundo_valor = input("Digite o segundo valor: ")

if primeiro_valor.isnumeric() and segundo_valor.isnumeric():
  
    primeiro_valor = int(primeiro_valor)
    segundo_valor = int(segundo_valor)

    if primeiro_valor > segundo_valor:
        menssagem = f'o  {primeiro_valor=} é maior que o  {segundo_valor=}'
    elif primeiro_valor == segundo_valor:
        menssagem = f'o valores são iguais'
    else:
        menssagem =  f'o  {segundo_valor=} é maior que o  {primeiro_valor=}'
else:
    menssagem = "Aceita apenas valores numéricos"

print(menssagem)