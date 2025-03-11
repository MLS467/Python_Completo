def valida_lista(lista):
    if not isinstance(lista,list):
        raise TypeError("Tipo deve ser lista")
    
def valida_tarefa(tarefa):
    if len(tarefa) == 0:
        raise Exception("Adicione uma tarefa!")
    
def valida_lista_vazia(lista):
     if len(lista) == 0:
        raise ValueError("Não há tarefas!")