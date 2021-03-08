print ("Exercício 3")
genero = input("Digite seu genero: (F para Feminino; M para masculino; nd para não quero definir) ")

if genero == "F" or genero == "f":
    print ("Sexo Feminino")
elif genero == "M" or genero == "m":
    print ("Sexo Masculino")
elif genero == "ND" or genero == "nd":
    print ("Não quero definir")
else:
    print ("Valor inválido")
    exit ()