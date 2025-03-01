"""
Fatiamento de strings
 012345678
 Olá mundo
-987654321
Fatiamento [i:f:p] [::]
i -> início
f -> final 
p -> passo
Obs.: a função len retorna a qtd 
de caracteres da str
"""

variavel = 'Olá mundo'
print(variavel[4:])
print(variavel[4:8])
print(variavel[:4+1])
print(variavel[-7:-3+1])

print(len(variavel))

print(variavel[0:len(variavel):4])
print(variavel[::-1])