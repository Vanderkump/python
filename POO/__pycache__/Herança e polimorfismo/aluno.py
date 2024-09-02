from histórico import Historico 
from pessoa import Pessoa

class Aluno(Pessoa):
    def __init__(self, cpf, matricula, nome, curso, disciplinas,
    disciplinas_disponiveis):
        super().__init__(nome, cpf, curso, disciplinas, disciplinas_disponiveis)
        self.matricula = matricula
        self.historico = Historico(self)

         
    def insere_disciplina(self, disciplina, disciplinas_disponiveis):
        if disciplina in disciplinas_disponiveis:
            self.disciplinas.append(disciplina)
            self.historico.disciplinas_cursadas.append(disciplina)
            return "Aluno foi matriculado na disciuplina{}".format(disciplina)
        else:
            return "Aluno não foi matriculado na disciuplina{}".format(disciplina)
        
    def remove_disciplina(self, disciplina, disciplina_disponiveis):
        for disc_disp in disciplina_disponiveis:
            if disciplina == disc_disp.nome:
                print("A disciplina esta na lista")
                self.disciplinas.remove(disc_disp)
                self.historico.disciplinas_cursadas.remove(disc_disp)