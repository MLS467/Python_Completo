frase = '           Olha que    ,  coisa interessante                 '

lista_frase_crua = frase.split(',')

nova_lista = []
for indice,valor in enumerate(lista_frase_crua):
    nova_lista.append(valor.strip())


print(lista_frase_crua)
print(nova_lista)

frase_junta = '-'.join(nova_lista)
print(frase_junta)