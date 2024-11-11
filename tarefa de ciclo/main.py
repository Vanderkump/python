from processo import Processo, ListaCircular
import time


def main():
    lista = ListaCircular()

    while True:
        
        nome = input("Digite o nome do processo (ou 'sair' para encerrar): ")
        if nome.lower() == 'sair':
            break
        
        prioridade = int(input("Digite a prioridade do processo (1-5): "))
        taxaPorCiclo = int(input("Digite a taxa por ciclo do processo (%): "))
        tempoProcessamento = int(input("Digite o tempo de processamento (em segundos): "))

       
        novo_process = Processo(nome, prioridade, 0, taxaPorCiclo, tempoProcessamento)

        
        lista.inserir(novo_process)

    
    while True:
        if not lista.processar():  
            break

    print("Todos os processos foram finalizados. Programa encerrado.")


if __name__ == "__main__":
    main()

