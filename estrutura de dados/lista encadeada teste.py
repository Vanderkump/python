class No():
    def __init__(self, num):
        self.num = num
        self.prox = None

class Lista():
    def __init__(self):
        self.cabeca = None

    def insere(self, num):
        novo_no = No(num)

        if self.cabeca == None:
            self.cabeca = novo_no

        aux = self.cabeca
        while(True):
            if aux == None or aux.num > num:
                break  
            aux = aux.prox

        if aux == self.cabeca: #primeiro elemento da lista
            novo_no.prox = self.cabeca
            self.cabeca = novo_no 
        #elif aux = None: #ultimo elemento
        #else: #elemento do meio 

    def imprime(self):
        aux = self.cabeca
        while(True):
            print(aux.num)
            aux = aux.prox

            if aux == None:
                break

lista = Lista()
lista.insere(5)
lista.insere(4)
lista.insere(3)
lista.insere(2)
lista.insere(1)
lista.imprime()