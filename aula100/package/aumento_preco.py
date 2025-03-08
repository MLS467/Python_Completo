def aumentar_preco(valores, aumento_porcento):
    porc = (100 + aumento_porcento) / 100
    novos_valores = [
       {**i, 'preco':round(i['preco'] * porc,2) }
        for i in valores
    ]
    return novos_valores