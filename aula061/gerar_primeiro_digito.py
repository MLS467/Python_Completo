
cpf_coletado = '963.276.630-01'
posicao_de_corte = cpf_coletado.index('-') if '-' in cpf_coletado else ''
nove_dig_limpo = cpf_coletado[:posicao_de_corte].replace('.','')

"""
contagem regressiva de 10 até 2
multiplicando os primeiros 9 dígitos antes do - 
"""

lista_digito_mult = []
count = 0
for multiplicador in range(10,1,-1):
    lista_digito_mult.append(int(nove_dig_limpo[count]) * multiplicador)
    count += 1

# conta com soma dos digitos multiplicado por 10 e pegando o resto %
resultado = sum(lista_digito_mult * 10) % 11

primeiro_digito_cpf = 0 if resultado > 9 else resultado


print(f"O primeiro dígito do CPF é {primeiro_digito_cpf}")

