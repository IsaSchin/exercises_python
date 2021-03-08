print ("Exercício 5")
a = float(input("Nota parcial 1: "))
b = float(input("Nota parcial 2: "))

if a > 10 or b > 10 or a < 0 or b < 0:
    print ("Nota(s) inválida(s)")
    exit ()

media = (a + b) / 2

if media >= 7 and media < 10:
    print (f"Sua média é {media} e você foi APROVADO!)")
elif media == 10:
    print (f"Sua média é 10 e você foi APROVADO COM DISTINÇÃO")
else:
    print (f"Sua média é {media} e você foi REPROVADO")