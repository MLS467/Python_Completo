lista = list(range(1,11))

def passa_proximo(list):
    while True:
        try:
            print(next(list))
        except StopIteration:
            break

def for_fajuto(list):
    nova_lista = iter(list)
    passa_proximo(nova_lista)

for_fajuto(lista)