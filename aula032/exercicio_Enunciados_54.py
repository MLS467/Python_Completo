"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
# numero_inteiro = input("Digite um numero inteiro: ")

# if not numero_inteiro.isnumeric():
#     print("Digite um número válido! ")
#     exit();

# teste_par_impar = float(numero_inteiro) % 2 == 0
# par_ou_impar = "Ímpar"

# if teste_par_impar:
#     par_ou_impar = "Par"


# print(f"O número é {par_ou_impar}")

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
hora_atual = input("Digite a hora atual: ")

# if not hora_atual.isnumeric():
#     print("Digite um número válido! ")
#     exit();

# try:
#     hora_atual = int(hora_atual)

#     hora_manha = hora_atual >= 0 and hora_atual <= 11
#     hora_tarde = hora_atual >=12 and hora_atual <= 17
#     hora_noite = hora_atual > 17 and hora_atual < 24
#     
# if hora_manha:
#        print("Bom dia !")
#     elif hora_tarde:
#        print("Boa Tarde !")
#     elif hora_noite:
#        print("Boa noite !")
#     else:
#        print("Hora inválida!")
# except:
#     print("O valor não é inteiro")

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

# nome_usuario = input("Digite seu nome aqui: ")

# nome_usuario = len(nome_usuario)

# if nome_usuario <= 4:
#    print("Seu nome é curto")
# elif nome_usuario <= 6:
#    print("Seu nome é normal")
# else:
#    print("Seu nome é muito grande")
