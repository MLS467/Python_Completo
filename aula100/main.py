import pprint

from package import produtos,aumentar_preco,faz_deepcopy,ordenar_valores

pprint.pprint(f"{"PRODUTOS":*^54}")
pprint.pprint(produtos)

novos_valores = faz_deepcopy(produtos)
resultado = aumentar_preco(novos_valores,10)
pprint.pprint(f"{"AUMENTO DE DEZ %":*^54}")
pprint.pprint(resultado)

produtos_ordenados_por_nome = faz_deepcopy(produtos)
ordenar_valores('nome',True,produtos_ordenados_por_nome)
print(f"{'ORDENADOS POR NOME DESC':*^50}")
pprint.pprint(produtos_ordenados_por_nome)

produtos_ordenados_por_preco = faz_deepcopy(produtos)
ordenar_valores('preco',False,produtos_ordenados_por_preco)
print(f"{'ORDENADOS POR PRECO':*^50}")
pprint.pprint(produtos_ordenados_por_preco)