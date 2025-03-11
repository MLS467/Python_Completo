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

from helpers import adicionar_nova_tarefa,listar
valores_validos = {'1','2','3','4'}

while True:
    # try:
        opcoes = input("1.Adicionar, 2.Listar, 3.Desfazer, 4.Refazer, 5.Sair ")

        if opcoes == '1':
            tarefa = input("Adicionar nova tarefa!")
            adicionar_nova_tarefa(tarefa)
        
        if opcoes == '2':
            listar()
        
        
        if opcoes == '5':
            break
        
    # except Exception as error:
    #     print(f"[ERRO] --> Saindo...")
    #     break

