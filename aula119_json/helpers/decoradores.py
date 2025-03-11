from helpers.exception.exception import valida_tarefa,valida_lista_vazia,valida_lista

def fabrica_dec_tarefa(lista):
    def dec_adicionar_tarefa(func):
        def nested_adicionar_tarefa(tarefa):
            try:
                valida_tarefa(tarefa)
                return func(tarefa,lista)
            except Exception as error:
                print(f"[ERRO] - {error}")
                return False
        return nested_adicionar_tarefa
    return dec_adicionar_tarefa


def dec_desfazer(func):
    def nested_desfazer(lista):
        try:
            valida_lista_vazia(lista)
            valida_lista(lista)
            return func(lista)
        except Exception as error:
            print(f"[ERRO] --> {error}")
    return nested_desfazer


def dec_listar(func):
    def nested_listar(lista):
        try:
            valida_lista_vazia(lista)
            return func(lista)
        except Exception as error:
            print(f"[ERRO] --> {error}")
    return nested_listar


def dec_refazer(func):
    def nested_refazer(*args):
        try:
            for arg in args:
                valida_lista(arg)
            valida_lista_vazia(args[1])
            return func(*args)
        except ValueError as error:
            print(f"[ERRO] Lixeira vazia --> {error}")
    return nested_refazer