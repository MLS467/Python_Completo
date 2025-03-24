from Model import Conta_Poupanca, Conta_Corrente, Cliente, Banco
import os

BANCOS = ['Brasil','Santander','Caixa']

print("1. Brasil, 2. Santander, 3. Caixa")
banco_escolhido = input("Tipo-> ")

print("1. Conta Corrente ou 2. Conta Poupança")
conta = input("Tipo de conta -> ")

c1 = Conta_Corrente(1,123,BANCOS[int(banco_escolhido) - 1],8) if conta == '1' else \
    Conta_Poupanca(1,123,BANCOS[int(banco_escolhido) - 1],8)

print("TIPO ->", type(c1))


print("Digite seu nome e idade")
nome = input("Nome-> ")
idade = input("idade-> ")


cliente = Cliente(nome,idade, c1)


banco = Banco(BANCOS[int(banco_escolhido) - 1], cliente)

def ver_saldo(conta): 
    print(conta.saldo)

def limpa_terminal():
    return os.system('cls' or 'clear')

try:
    while True:

        print("[1] Sacar,\n[2] Depositar,\n[3] Consultar Saldo,\n[4] finalizar")
        
        acao = input("Digite a ação -> ")

        if acao == '1':
            if not banco.autenticar():
                raise ValueError("Usuario não autenticado")
            limpa_terminal()
            valor_sacar = input("Valor para saque -> R$")
            cliente.conta.sacar(float(valor_sacar))
        
        elif acao == '2':
            limpa_terminal()
            valor_depositar = input("Valor para deposito -> R$")
            cliente.conta.depositar(float(valor_depositar))

        elif acao == '3':
            limpa_terminal ()
            print(banco)

        elif acao == '4':
            print("Operação finalizada com sucesso !")
            break
except ValueError as error:
    limpa_terminal()
    print(f"ERRO {error}")