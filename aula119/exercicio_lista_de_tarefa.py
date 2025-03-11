# Exercício - Lista de tarefas com desfazer e refazer
 # Música para codar =)
 # Everybody wants to rule the world - Tears for fears
 # todo = [] -> lista de tarefas
 # todo = ['fazer café'] -> Adicionar fazer café
 # todo = ['fazer café', 'caminhar'] -> Adicionar caminhar
 # desfazer = ['fazer café',] -> Refazer ['caminhar']
 # desfazer = [] -> Refazer ['caminhar', 'fazer café']
 # refazer = todo ['fazer café']
 # refazer = todo ['fazer café', 'caminhar']
import os

from helpers import adicionar_tarefa_main,listar_main,desfazer_main,refazer_main
valores_validos = {'1','2','3','4'}

while True:
    try:
        opcoes = input("1.Adicionar, 2.Listar, 3.Desfazer, 4.Refazer, 5.Sair ")

        operacoes = {
            '1':lambda:adicionar_tarefa_main(),
        }
        os.system('cls')
        
        if opcoes not in valores_validos:
            raise ValueError("Opção inválida! ")
        else:
            operacoes.get(opcoes)()  

    except Exception as error:
        print(f"[ERRO] --> Saindo...")
        break

