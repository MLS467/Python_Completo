nome = "Maisson Leal da Silva"

count = 0
novo_nome = ''
while count < len(nome):
    novo_nome += f"*{nome[count]}"
    count+=1

novo_nome += '*'
print(novo_nome)