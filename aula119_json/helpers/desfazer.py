from helpers.db.mockado import lista_de_tarefas,lixeira
from helpers.decoradores import dec_desfazer

@dec_desfazer
def desfazer_tarefa(lista):
    tarefa_removida = lista.pop()
    return tarefa_removida

def desfazer_main():
   resultado = desfazer_tarefa(lista_de_tarefas)
   
   if resultado is not None:
        lixeira.append(resultado)
        print('lixeira --->', lixeira)
        print(f"{resultado} foi removido com sucesso!")