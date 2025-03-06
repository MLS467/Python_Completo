lista = ['a',1,1.1,True, [0,1,2], (1,2),{0,1},{'nome':'Luiz'}]


for i in lista:
    if isinstance(i, str):
        print(i)

    if isinstance(i, set):
        print(i)

# print(teste)
