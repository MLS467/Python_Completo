def multiplica(*args):
    acum = 1
    for i in args:
        acum *= i
    return acum

total = multiplica(1,2,5,6)
print(total)


def par_impar(valor):
        return 'Ímpar' if not valor % 2 == 0 else 'Par'


resultado = par_impar(252)
print(resultado)
