print ("Hello World")
a = float(input("Nota parcial 1: "))
b = float(input("Nota parcial 2: "))

media = (a + b) / 2

if media >= 7 and media < 10:
    print (f"Sua média é {media} e você foi APROVADO!)")
elif media >= 10:
    print (f"Sua média é 10 e você foi APROVADO COM DISTINÇÃO")
else:
    print (f"Sua média é {media} e você foi REPROVADO")