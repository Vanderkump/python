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
            return

        aux = self.cabeca
        while(True):
            if aux.prox == None or aux.prox.num > num:
                break
            aux = aux.prox

        if aux.prox == None: #último elemento
            aux.prox = novo_no
        elif aux == self.cabeca and num < aux.num: #primeiro elemento
            novo_no.prox = self.cabeca
            self.cabeca = novo_no
        else: #elemento do meio
            novo_no.prox = aux.prox
            aux.prox = novo_no

    def imprime(self):
        aux = self.cabeca
        print("\n\n")
        while(True):
            print(aux.num)
            aux = aux.prox

            if aux == None:
                break


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