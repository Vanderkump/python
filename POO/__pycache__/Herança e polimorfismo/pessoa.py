class Pessoa():
    def __init__(self, nome, cpf, curso, disciplinas, disciplinas_disponiveis,
    salario=0):
        self.nome = nome
        self.cpf = cpf
        self.curso = curso
        self.salario = salario
        self.disciplinas = []
        
        for disc in disciplinas:
            for disc_disp in disciplinas_disponiveis:
                if disc == disc_disp.nome:
                    self.disciplinas.append(disc_disp)

    def define_bonus(self):
        return self.salario + 2000
    
@property
def nome(self):
        return self._nome

@cpf.setter
def cpf(self, cpf):
        self._cpf = cpf

@curso.setter
def curso(self, curso):
        self._curso = curso

@property
def disciplinas(self):
        return self._disciplinas 

@salario.setter
def salario(self, salario):
        self._salari = salario