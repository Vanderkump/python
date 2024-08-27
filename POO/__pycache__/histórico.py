import datetime

class Historico():
    def __init__(self):
        self.data_matricula = datetime.datetime.today()
        self.disciplinas_cursadas = []

    def imprime(self):
        print("Histórico do aluno")
        for h in self.disciplinas_cursadas:
            print("Disciplina {} com {} horas cursadas".format(h.nome,h.carga_horaria))
