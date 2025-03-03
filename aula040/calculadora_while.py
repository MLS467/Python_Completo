sair = False

while not sair:
    # pegando valores do usuário
    primeiro_numero = input("Primeiro valor ")
    segundo_numero = input("Segundo valor ")
    operacao = input("soma [1].  subtração [2]. multiplicação [3]. divisão [4]. ")
    
    # testando operadores
    operadores_validos = '1234'

    if operacao not in operadores_validos:
        print("Operador inválido !")
        continue

    if len(operacao) > 1:
        print("Apenas 1 operação! ")
        continue

    # testando valores vazios ou não numéricos
    teste_valores_numericos = (not primeiro_numero.isnumeric() or not segundo_numero.isnumeric() or \
        not operacao.isnumeric())
    
    teste_valores_vazios = (not primeiro_numero or not segundo_numero or not operacao) 
    
    valores = teste_valores_numericos or teste_valores_vazios

    controle = True

    if valores:
        msg = "Preencha todos os campos com valores válidos!"
        print(f"{msg:*^100}")
        continue

    # convertendo para números
    primeiro_numero = float(primeiro_numero)
    segundo_numero = float(segundo_numero)

    # realizando operações
    if operacao == '1':
        print(primeiro_numero+segundo_numero)
    
    if operacao == '2':
        print(primeiro_numero-segundo_numero)

    if operacao == '3':
        print(primeiro_numero*segundo_numero)
    
    if operacao == '4' and segundo_numero != 0:
        print(primeiro_numero / segundo_numero)
    elif operacao == '4' and segundo_numero == 0:
        print("Não pode dividir por zero!")

    # Verificando se quer continuar ou não
    sair = input("[S]air ? ").lower().startswith('s')
    controle = False



