frase = 'O Python é uma linguagem de programação '\
'multiparadigma. '\
'Python foi criado por Guido Van Rossum'

frase = frase.lower().replace(' ', '')
qtd_vezes = 0
letra = ''
i = 0

while i < len(frase):

    valor_numero = frase.count(frase[i])

    if valor_numero > qtd_vezes:
        letra = frase[i]
        qtd_vezes = valor_numero
    
    i += 1

print(f"A letra que mais aparece é * { letra } * e aparece {qtd_vezes} vezes")
