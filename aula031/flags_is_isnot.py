"""
Flag (Bandeira) - Marca um local
None = Não valor
is e is not = é ou não é (tipo,valor,identidade)
id = Identidade

"""

condicao = True
flag = None


if condicao:
    flag = True
    print("Faça algo")
else:
    print("Não faça algo")

if flag is None:
    print("Não passou no if")

if flag is not None:
    print(f"Passou no if valor é {flag}")