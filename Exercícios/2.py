'''
Faça um Programa que pergunte quanto um trabalhador ganha por hora e o número de
horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês,
sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5%
para o sindicato, faça um programa que imprima:
1 – o salário bruto
2 – total pago ao INSS
3 – total pago ao sindicato
4 - o salário líquido
salário bruto - descontos
'''
salario = int(input("Quanto o funcionario ganha por hora?"))
hora = int(input("Quantas horas o funcionário trabalhou?"))

SaldoBruto = salario * hora
Inss = round(SaldoBruto * (8/100))
Sindicato = (SaldoBruto * (5/100))
SaldoLiquido = (SaldoBruto - (SaldoBruto * (5/100)) + (SaldoBruto - (SaldoBruto * (8/100))) + (SaldoBruto - (SaldoBruto * (11/100))))

print(f"salario bruto: {SaldoBruto}\n inss: {Inss}\n Sindicato: {Sindicato}\n SaldoLiquido: {SaldoLiquido}")
