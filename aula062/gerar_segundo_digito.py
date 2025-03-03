cpf_coletado = '042.661.300-74'

posicao_de_corte = cpf_coletado.index('-') if '-' in cpf_coletado else ''
nove_dig_limpo = cpf_coletado[:posicao_de_corte].replace('.','')

teste_digito_iguais = nove_dig_limpo[0] * len(nove_dig_limpo) == nove_dig_limpo

if teste_digito_iguais:
    print("CPF com todos dígitos repetidos não é válido! ")
    exit()

"""
contagem regressiva de 10 até 2
multiplicando os primeiros 9 dígitos antes do '-- 
"""

lista_digito_mult = []
count = 0
for multiplicador in range(10,1,-1):
    lista_digito_mult.append(int(nove_dig_limpo[count]) * multiplicador)
    count += 1

# conta com soma dos digitos multiplicado por 10 e pegando o resto %
resultado = sum(lista_digito_mult * 10) % 11

primeiro_digito_cpf = 0 if resultado > 9 else resultado

"""
contagem regressiva de 11 até 2
multiplicando os primeiros 9 dígitos mais o primeiro dígito 
"""
nove_digitos_limpos_2 = nove_dig_limpo +  str(primeiro_digito_cpf)
count_2 = 11

lista_digito_mult_2 = []

for digitos in nove_digitos_limpos_2:
    lista_digito_mult_2.append(int(digitos) * count_2)
    count_2 -= 1

# conta com soma dos digitos multiplicado por 10 e pegando o resto %
resultado_2 = sum(lista_digito_mult_2) * 10 % 11


segundo_digito_cpf = 0 if resultado_2 > 9 else resultado_2



cpf_coletado_teste = cpf_coletado.replace('.','').replace('-','');
dois_digito = str(primeiro_digito_cpf) + str(segundo_digito_cpf)


cpf_gerado = nove_dig_limpo + dois_digito


if cpf_gerado == cpf_coletado_teste:
    print(f"CPF {cpf_gerado} é válido")
else:
    print("CPF Inválido")