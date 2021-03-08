print ("Exercício 10")
turno = input("Qual o período em que você estuda? Digite M para matutino, V para vespertino e N para noturno: ")

if turno == "M" or turno == "m":
    print ("Bom dia!")
elif turno == "V" or turno == "v":
    print ("Boa tarde!")
elif turno == "N" or turno == "n":
    print ("Boa noite!")
else:
    print ("Valor inválido!")