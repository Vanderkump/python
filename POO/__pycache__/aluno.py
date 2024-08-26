class Aluno:
    def __init__(self, matricula,nome,curso,disciplinas, disciplina_disponiveis):
        self.matricula = matricula
        self.nome = nome
        self.curso = curso
        self.disciplinas = []

        for disc in disciplinas:
            for disc_disp in disciplina_disponiveis:
                if disc == disc_disp.nome:
                    self.disciplinas = disciplinas.append(disc)
                    print("Aluno {} foi matriculado na disciplina {}". format(self.nome, disc))
                    break
                else:
                    print("Aluno {} não foi matriculado na disciplina {}". format(self.nome, disc))

    def insere_disciplina(self, disciplina):
        if disciplina in disciplinas_disponiveis:
            self.disciplinas.append(disciplina)
            return "Aluno foi matriculado na disciuplina{}".format(disciplina)
        else:
            return "Aluno não foi matriculado na disciuplina{}".format(disciplina)