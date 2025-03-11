from helpers.db.mockado import lista_de_tarefas
from helpers.decoradores import dec_listar


@dec_listar
def listar(lista):
    for index,tarefa in enumerate(lista):
        print(f"{index + 1} --> {tarefa}")

def listar_main():
    listar(lista_de_tarefas)