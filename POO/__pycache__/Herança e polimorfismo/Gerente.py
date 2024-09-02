from Funcionario import Funcionario
from pessoa import Pessoa

class Gerente(Pessoa):
    def __init__(self, nome, cpf, salario, senha,login, qtd_gerenciados):
        super().__init__(nome, cpf, salario)
        self.login = login
        self._senha = senha
        self._qtd_gerenciados = qtd_gerenciados

gerente = Gerente("Neymar", "22016787656", 50000, "senha", "neyfilho", 10)