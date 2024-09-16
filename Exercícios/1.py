"""
Faça um programa que leia 2 números do teclado e imprima na tela
Sua soma
Sua subtração
Verifique qual número é menor e faça (maior-menor)
Sua divisão
Verifique se o denominador é zero e imprima uma
mensagem na tela (não é possível dividir por zero)
sua multiplicação
"""

num1 = int(input("digite um número: ")) 
num2 = int(input("digite o segundo número: "))

soma = num1 + num2
subtração = num1 - num2
maior = max(num1, num2)
divisão = num1 / num2
multiplicação = num1 * num2 

if(divisão != 0):
    print("não tem resto zero")
else:
     print("tem resto zero")

print(soma, subtração, maior, divisão, multiplicação)
