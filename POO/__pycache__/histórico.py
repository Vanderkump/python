import datetime

class Historico():
    def __init__(self, aluno):
        self.data_matricula = datetime.datetime.today()
        self.disciplinas_cursadas = []
        self.aluno = aluno

    def imprime_historico(self):
        print("Histórico do aluno {}".format(self.aluno.matricula))
        for h in self.disciplinas_cursadas:
            print("Disciplina {} com {} horas cursadas".format(h.nome,h.carga_horaria))
