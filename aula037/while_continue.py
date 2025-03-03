contador = 0


while contador < 100:
    contador += 1

    if contador >= 50 and contador <= 70:
        continue

    if contador == 5:
        print("Sem 5")
        continue

    print(contador)

print("Acabou!")