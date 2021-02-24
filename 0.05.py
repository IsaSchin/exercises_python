print ("Hello World") # pode remover essa linha

a = float(input("Nota parcial 1: "))
b = float(input("Nota parcial 2: "))

# nota 13 e -4, por exemplo, não existem. Faltou a verificação do input
# a nota inserida tem que ser positiva e de valor entre 0 e 10!

media = (a + b) / 2

if media >= 7 and media < 10: # correto
    print (f"Sua média é {media} e você foi APROVADO!)")
elif media >= 10: # <--- a media nunca deve ser maior que 10
    print (f"Sua média é 10 e você foi APROVADO COM DISTINÇÃO")
else: # correto
    print (f"Sua média é {media} e você foi REPROVADO")
