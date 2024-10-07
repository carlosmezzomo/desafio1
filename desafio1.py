from datetime import datetime

class ContaBancaria:
    def __init__(self):
        self.saldo = 0.0
        self.depositos = []
        self.saques = []
        self.limite_saque = 500.00
        self.saque_diario = 0
        self.max_saques_diarios = 3

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            self.depositos.append((valor, datetime.now()))
            print(f"Depósito de R$ {valor:.2f} realizado com sucesso.")
        else:
            print("Valor de depósito deve ser positivo.")

    def sacar(self, valor):
        if self.saque_diario >= self.max_saques_diarios:
            print("Limite de saques diários atingido.")
            return
        if valor > self.limite_saque:
            print(f"Valor do saque não pode exceder R$ {self.limite_saque:.2f}.")
            return
        if valor > self.saldo:
            print("Saldo insuficiente para realizar o saque.")
            return
        
        self.saldo -= valor
        self.saques.append((valor, datetime.now()))
        self.saque_diario += 1
        print(f"Saque de R$ {valor:.2f} realizado com sucesso.")

    def extrato(self):
        print("\n=== Extrato Bancário ===")
        if not self.depositos and not self.saques:
            print("Não foram realizadas movimentações.")
        else:
            for deposito in self.depositos:
                valor, data = deposito
                print(f"Depósito: R$ {valor:.2f} em {data.strftime('%d/%m/%Y %H:%M:%S')}")
            for saque in self.saques:
                valor, data = saque
                print(f"Saque: R$ {valor:.2f} em {data.strftime('%d/%m/%Y %H:%M:%S')}")
        print(f"Saldo atual: R$ {self.saldo:.2f}")
        print("========================\n")

# Exemplo de uso
def main():
    conta = ContaBancaria()

    while True:
        print("Bem-vindo ao Sistema Bancário!")
        print(f"Saldo atual: R$ {conta.saldo:.2f}")
        print("1. Depositar")
        print("2. Sacar")
        print("3. Extrato")
        print("4. Sair")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            valor = float(input("Digite o valor a ser depositado: "))
            conta.depositar(valor)
        elif opcao == "2":
            valor = float(input("Digite o valor a ser sacado: "))
            conta.sacar(valor)
        elif opcao == "3":
            conta.extrato()
        elif opcao == "4":
            print("Saindo do sistema. Até logo!")
            break
        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    main()
