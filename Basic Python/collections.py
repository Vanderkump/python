familia = ["Felipe", "Davi", "Heitor", "Fabiana"]

print(familia[0])
familia.append("Turmalina")
print(familia)

familia.extend(["Ametista","José"])
print(familia)

familia.insert(2, "Carla")
print(familia)

familia.remove("Felipe")
print(familia)

familia.index("José")

print(familia.count("Ametista"))

idade_familia = [12, 56 , 37, 8]
print(idade_familia)
idade_familia.sort()
print(idade_familia)
idade_familia.reverse()
print(idade_familia)

familia2 = familia.copy()
print(familia2)
familia.remove("Fabiana")
print(familia)
print(familia2)

coordenadas = (-49, -36) #tuple não pode ser alterado o valor