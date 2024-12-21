class ContaBancaria:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f"Depósito de R${valor:.2f} realizado com sucesso :))")
        else:
            print("Valor de depósito inválido.")

    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            print(f"Saque de R${valor:.2f} realizado com sucesso!")
        else:
            print("Saldo insuficiente para realizar o saque :((")

    def exibirSaldo(self):
        print(f"Saldo atual de {self.titular}: R${self.saldo:.2f}")


conta1 = ContaBancaria("Gabriel", 100)
conta1.exibirSaldo()
conta1.depositar(200)
conta1.sacar(100)
conta1.exibirSaldo()

conta2 = ContaBancaria("Anna Clara")
conta2.exibirSaldo()
conta2.depositar(300)
conta2.exibirSaldo()
