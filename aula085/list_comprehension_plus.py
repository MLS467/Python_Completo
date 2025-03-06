numero = list(range(10))

nova_lista = [
    el if el != 6 else 600
    for el in numero 
    if el % 2 == 0
]

nome = ['luiz', 'maria','helena','joana','felipe']

novos_nomes = [
    f"{n[:-1].lower()}{n[-1].upper()}"

    for n in nome
]
print(novos_nomes)