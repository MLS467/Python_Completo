pessoas = [
    {'nome':'maisson','idade':29},
    {'nome':'luciane','idade':32},
    {'nome':'manuelle','idade':4}
]

# nova_lista = [
#     {**pessoa, 'idade':pessoa['idade']+1}
#     if pessoa['idade'] > 20 else {**pessoa}
#     for pessoa in pessoas
# ]

nova_lista = [
    {**p,'idade':p['idade']+1} if p['idade'] > 10 else {**p}
    for p in pessoas
]


print(*nova_lista, sep="\n")

