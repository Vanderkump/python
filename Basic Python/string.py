minha_string = "programação"
outra_string = "felipe,\ncagou,\nse limpou"

print(f"felipe gosta de {minha_string}")

print(minha_string.upper()) #todas as letras maisculas
print(minha_string.lower()) #todas as letras minusculas 
print("---------------------------------------------------------------")
print(minha_string.isupper()) #verificar se a string é maiscula 
print(minha_string.islower()) #verificar se a string é minuscula
print("---------------------------------------------------------------")
print(minha_string.strip()) #verificar se a string é minuscula
print(minha_string.replace("pro", "")) #modifica a str com a parte que vc quer modificar e oq vc quer modificar
print("---------------------------------------------------------------")
print(len(minha_string)) # tamanho da string
print(minha_string[-7:-3]) # retorna as letras com os indices 
print("---------------------------------------------------------------")
print(minha_string.index("p")) #retorna o indice da letra
x = "pro" in minha_string # verifica se a sua str tem o conteudo da variavel 
print(x)
print("---------------------------------------------------------------")
print(outra_string)