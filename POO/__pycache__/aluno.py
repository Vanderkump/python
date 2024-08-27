from histórico import Historico 

class Aluno:
    def __init__(self, matricula,nome,curso,disciplinas, disciplina_disponiveis):
        self.matricula = matricula
        self.nome = nome
        self.curso = curso
        self.disciplinas = []
        self.historico = Historico(self)

        for disc in disciplinas:
            for disc_disp in disciplina_disponiveis:
                if disc == disc_disp.nome:
                    self.disciplinas.append(disc_disp)
                    self.historico.disciplinas_cursadas.append(disc_disp)
                    print("Aluno {} foi matriculado na disciplina {}". format(self.nome, disc))
                    break
                else:
                    print("Aluno {} não foi matriculado na disciplina {}". format(self.nome, disc))
        
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