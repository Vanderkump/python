class No():
    def __init__(self, num):
        self.num = num
        self.prox = None

class Lista():
    def __init__(self):
        self.cabeca = None

    def insere(self, num):
        novo_no = No(num)

        # Se a lista estiver vazia, insira o novo nó como cabeça
        if self.cabeca == None:
            self.cabeca = novo_no
            return

        # Se o novo elemento for menor que o primeiro elemento (cabeça), insira no início
        if num < self.cabeca.num:
            novo_no.prox = self.cabeca
            self.cabeca = novo_no
            return

        # Caso contrário, encontrar o local correto de inserção (meio ou fim)
        aux = self.cabeca
        while aux.prox is not None and aux.prox.num < num:
            aux = aux.prox
        
        # Agora insere o novo nó no local apropriado
        novo_no.prox = aux.prox
        aux.prox = novo_no

    def imprime(self):
        aux = self.cabeca
        while aux is not None:
            print(aux.num)
            aux = aux.prox

# Testando a lógica
lista = Lista()
lista.insere(5)
lista.insere(4)
lista.insere(3)
lista.insere(2)
lista.insere(1)
lista.insere(6)  # Inserindo no final
lista.insere(0)  # Inserindo no início
lista.insere(4.5) # Inserindo no meio
lista.imprime()
