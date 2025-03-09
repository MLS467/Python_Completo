import itertools
import pprint

def exibir(iterator):
    print(*list(iterator), sep="\n")
# for i in itertools.count(100,10):
#     print(i)


nome = ["Maisson",'Manuelle','Luciane','Lucia','Lori']
combinacao = list(itertools.combinations(nome,2))

# exibir(combinacao)

permutacao = itertools.permutations(nome,2)

# exibir(permutacao)

camisetas = [
     ['preta', 'branca'],
     ['p', 'm', 'g'],
     ['masculino', 'feminino', 'unisex'],
     ['algodão', 'poliéster'],
     ['19.99','22.50']
 ]

exibir(itertools.product(*camisetas))



