# senha_salva = '12345'
# senha_digitada = ''
# repeticoes = 0

# while senha_digitada != senha_salva:
#     senha_digitada = input(f"Digite sua senha, tentativa {repeticoes}X ")
#     repeticoes += 1
# print(repeticoes)
# print('Esse laço pode ser infinito! ')

texto = 'Python'

# for index in texto:
#     print(index)

# teste = [1,2,3,4,5,6,8,7,9]

# for i in teste:
#     print(i)

novo_texto = ''
for letra in texto:
    novo_texto += f"*{letra}"
    print(letra)

novo_texto += '*'

print(novo_texto)