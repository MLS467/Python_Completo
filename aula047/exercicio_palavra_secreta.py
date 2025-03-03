"""
Faça um jogo para o usuário adivinhar qual
a palavra secreta.
- Você vai propor uma palavra secreta
qualquer e vai dar a possibilidade para
o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você 
vai conferir se a letra digitada está
na palavra secreta.
    - Se a letra digitada estiver na
    palavra secreta; exiba a letra;
    - Se a letra digitada não estiver
    na palavra secreta; exiba *.
Faça a contagem de tentativas do seu
usuário.
"""

import os

palavra_oculta = "Testando".lower()

palavra_secreta = '*' * len(palavra_oculta)
tentativas = 0

while '*' in palavra_secreta:
    letra_digitada = input('Digite uma letra ').lower()
    nova_palavra = ''

    if len(letra_digitada) > 1:
        print('Digite apenas uma letra por vez ')
        continue
    
    for i in range(len(palavra_oculta)):
        if letra_digitada == palavra_oculta[i]:
            nova_palavra += letra_digitada
        else:
            nova_palavra += palavra_secreta[i]
    
    tentativas += 1 
    
    palavra_secreta = nova_palavra
    print(palavra_secreta)

else:
    os.system('cls' or 'clear')
    print(f"Parabéns a palavra secreta era {palavra_oculta=} com {tentativas=}X")
             






