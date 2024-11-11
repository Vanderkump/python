import time


class Processo:
    def __init__(self, nome, prioridade, taxaCompleto, taxaPorCiclo, tempoProcessamento):
        self.nome = nome
        self.prioridade = prioridade
        self.taxaCompleto = taxaCompleto
        self.taxaPorCiclo = taxaPorCiclo
        self.tempoProcessamento = tempoProcessamento  
        self.prox = None
    
    def atualizar_taxa(self):
        
        self.taxaCompleto += self.taxaPorCiclo
        if self.taxaCompleto > 100:
            self.taxaCompleto = 100
    
    def __str__(self):
        
        return f"{self.nome} - Prioridade {self.prioridade} - {self.taxaCompleto}% Completo"



class ListaCircular:
    def __init__(self):
        self.head = None
    
    def inserir(self, processo):
        
        if not self.head:
            self.head = processo
            processo.prox = self.head
        else:
            atual = self.head
            while atual.prox != self.head and atual.prioridade < processo.prioridade:
                atual = atual.prox
            processo.prox = atual.prox
            atual.prox = processo
            
           
            if processo.prioridade < self.head.prioridade:
                self.head = processo

    def remover(self, processo):
       
        if self.head is None:
            return
        
        if self.head == processo:
            if self.head.prox == self.head:  
                self.head = None
            else:
                
                atual = self.head
                while atual.prox != self.head:
                    atual = atual.prox
                self.head = self.head.prox
                atual.prox = self.head
        else:
            atual = self.head
            while atual.prox != self.head and atual.prox != processo:
                atual = atual.prox
            if atual.prox == processo:
                atual.prox = processo.prox

    def processar(self):
        
        if not self.head:
            print("Todos os processos foram finalizados.")
            return False  
        
        atual = self.head
        while atual:
            
            print(f"{atual.nome} entrou no processador")
            time.sleep(atual.tempoProcessamento)  
            atual.atualizar_taxa()  
            print(f"{atual.nome} saiu do processador com taxa de {atual.taxaCompleto}%")

            if atual.taxaCompleto >= 100:
                print(f"{atual.nome} foi finalizado")
                self.remover(atual)  

            
            if self.head is None:  
                return False

            if atual.prox == self.head:  
                break
            atual = atual.prox
        
        return True 
