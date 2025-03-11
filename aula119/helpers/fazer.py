from helpers.exception.exception import valida_tarefa
from helpers.db.mockado import lista_de_tarefas
from helpers.decoradores import fabrica_dec_tarefa

@fabrica_dec_tarefa(lista_de_tarefas)
def adicionar_tarefa(tarefa,lista=None):
    lista.append(tarefa)
    return True

def adicionar_tarefa_main():
    nova_tarefa = input("Adicionar nova tarefa: ")
    adicionar_tarefa(nova_tarefa)
    print(f"{nova_tarefa} adicionada com sucesso! ")