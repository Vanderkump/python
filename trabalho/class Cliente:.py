class Cliente:
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf
    
    @staticmethod
    def criar_cliente(nome, cpf):
        return Cliente(nome, cpf)

class Historico:
    def __init__(self):
        self.transacoes = []

    def adicionar_transacao(self, transacao):
        self.transacoes.append(transacao)

    def imprimir_historico(self):
        print("Histórico de transações:")
        for transacao in self.transacoes:
            print(transacao)

class Conta:
    def __init__(self, numero, agencia, cliente):
        self.numero = numero
        self.agencia = agencia
        self.cliente = cliente
        self.saldo = 0
        self.historico = Historico()

    @staticmethod
    def criar_conta(numero, agencia, cliente):
        return Conta(numero, agencia, cliente)

    def saque(self, valor):
        if valor > self.saldo:
            print("Saldo insuficiente para o saque.")
        else:
            self.saldo -= valor
            self.historico.adicionar_transacao(f"Saque de R${valor:.2f}")
            print(f"Saque de R${valor:.2f} realizado com sucesso.")

    def deposito(self, valor):
        self.saldo += valor
        self.historico.adicionar_transacao(f"Depósito de R${valor:.2f}")
        print(f"Depósito de R${valor:.2f} realizado com sucesso.")

    def extrato(self):
        print(f"Extrato da conta {self.numero} - Agência {self.agencia}")
        print(f"Cliente: {self.cliente.nome}")
        print(f"CPF: {self.cliente.cpf}")
        print(f"Saldo atual: R${self.saldo:.2f}")
        self.historico.imprimir_historico()

cliente = Cliente.criar_cliente("João Silva", "123.456.789-00")
conta = Conta.criar_conta("1234", "001", cliente)

conta.deposito(500)
conta.saque(200)
conta.saque(400)
conta.extrato()
