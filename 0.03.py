print ("Hello World") #pode remover essa linha
genero = input("Digite seu genero (F / M / não quero definir): ")

if genero == "F":
    print ("Sexo Feminino")
elif genero == "f":
     print ("Sexo Feminino")
elif genero == "M":
    print ("Sexo Masculino")
elif genero == "m":
    print ("Sexo Masculino")
else:
    print ("Não quero definir")

# => está correto.. só uma dica de otimização:
#
# essas 4 condições podem ser alteradas pra 2:
#
# if genero == "F" or genero == "f":
#    print ("Sexo Feminino")
#
# o mesmo pode ser feito com os outros 2

# outra coisa:
# faltou uma parte do exercicio em que ele pede pra vc dizer que qualquer outro valor digitado não é valido.
# no caso, pode ter 3 inputs (m/f/n) mas caso for digitado algum alem desses, a mensagem tem que ser "opcao invalida"
