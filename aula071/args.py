# def somador(*args):
#     return sum(args)

# total = somador(1,2,3,45,6,5,4)

# print(total)


def somador(*args):
    acum = 0
    for i in args:
        acum += i
    return acum

total = somador(1,2,3,45,6,5,4)

print(total)