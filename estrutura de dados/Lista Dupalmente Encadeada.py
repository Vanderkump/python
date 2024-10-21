class No():
    def __init__(self, num):
        self.num = num
        self.prox = None
        self.ant = None 

class Lista():
    def __init__(self):
        self.cabeca = None

    def insere(self, num):
        novo_no = No(num)

        if self.cabeca is None:  
            self.cabeca = novo_no
            return

        aux = self.cabeca
        while True:
            if aux.prox is None or aux.prox.num > num:
                break
            aux = aux.prox

        if aux.prox is None:  
            aux.prox = novo_no
            novo_no.ant = aux
        elif aux == self.cabeca and num < aux.num:  
            novo_no.prox = self.cabeca
            self.cabeca.ant = novo_no
            self.cabeca = novo_no
        else:  
            novo_no.prox = aux.prox
            novo_no.ant = aux
            aux.prox.ant = novo_no
            aux.prox = novo_no

    def imprime(self):
        aux = self.cabeca
        print("\nLista (do primeiro ao último):")
        while aux:
            print(aux.num)
            aux = aux.prox

        aux = self.cabeca
        print("Lista (do último ao primeiro):")
        while aux.prox:  
            aux = aux.prox
        
        while aux:
            print(aux.num)
            aux = aux.ant


lista = Lista()
lista.insere(47)
lista.imprime()
lista.insere(68)
lista.imprime()
lista.insere(67)
lista.imprime()
lista.insere(69)
lista.imprime()
lista.insere(22)
lista.imprime()
lista.insere(8)
lista.imprime()
lista.insere(39)
lista.imprime()
lista.insere(42)
lista.imprime()
lista.insere(56)
lista.imprime()
lista.insere(90)
lista.imprime()
