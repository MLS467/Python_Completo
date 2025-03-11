from helpers.db.mockado import lista_de_tarefas,lixeira
from helpers.decoradores import dec_refazer

@dec_refazer
def refazer(lista_tarefas, lista_lixeira):
    tarefa_removida = lista_lixeira.pop()
    lista_tarefas.append(tarefa_removida)
    return tarefa_removida

def refazer_main():
    valor_refeito = refazer(lista_de_tarefas,lixeira)
    print(f"A tarefa {valor_refeito} foi restaurada")
