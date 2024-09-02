import datetime

class Historico():
    def __init__(self, aluno):
        self.data_matricula = datetime.datetime.today()
        self.disciplinas_cursadas = []
        self.aluno = aluno

    def imprime_historico(self):
        print("Histórico do aluno: matricula: {} nome: {}".format(self.aluno.matricula, self.aluno.nome))
        for h in self.disciplinas_cursadas:
            print("Disciplina {} com {} horas cursadas".format(h.nome,h.carga_horaria))
