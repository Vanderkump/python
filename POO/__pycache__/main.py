from aluno import Aluno
from disciplina import Disciplina

disciplina_disponiveis = []

disc = Disciplina("POO", "Alyson", 64, "LEC1")
disciplina_disponiveis.append(disc)

disc = Disciplina("Matemática", "Roberto Carlos", 32, "I2118")
disciplina_disponiveis.append(disc)

aluno = Aluno("22016733730", "Felipe", "ECA", ["POO", "tecnicas de programação", "Eletronica"], disciplina_disponiveis)
aluno1 = Aluno("09354687390", "julia", "ECA", ["POO", "tecnicas de programação"], disciplina_disponiveis)

print(aluno.disciplinas)
print(aluno1.disciplinas)

print(aluno.insere_disciplina("Ciências Humanas", disciplina_disponiveis))

aluno.remove_disciplina("POO", disciplina_disponiveis)
    

