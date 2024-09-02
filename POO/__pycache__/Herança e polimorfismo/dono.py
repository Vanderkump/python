from Gerente import Gerente

class Dono(Gerente):
    def __init__(self, nome, cpf, salario, senha,login, qtd_gerenciados, cnpj):
        super().__init__(nome, cpf, salario, senha, login, qtd_gerenciados)
        self.cnpj = cnpj
