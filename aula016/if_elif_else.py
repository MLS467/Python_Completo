# if  /    elif  / else
# se / se não se/ se não

val = 1

while True:
    entrada = input("Digite entrar ou sair do sistema! ")

    if entrada == 'entrar':
        print('Entrou no sistema')
        break
    elif entrada == 'sair':
        print('Saiu no sistema')
        break
    else:
        print('Digite um valor válido')
