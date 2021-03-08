print ("Exercício 9")
print ("Digite três números para serem colocados em ordem decrescente")
num1 = float(input("Digite seu primeiro número: "))
num2 = float(input("Digite seu segundo número: "))
num3 = float(input("Digite seu terceiro número: "))

if num1 > num2 and num1 > num3:
        if num2 > num3:
            print ("Os números em ordem decrescente são: ", num1, num2, num3)
        if num2 < num3:
            print ("Os números em ordem decrescente são: ", num1, num3, num2)
if num3 > num2 and num3 > num1:
        if num2 > num1:
            print ("Os números em ordem decrescente são: ", num3, num2, num1)
        if num2 < num1:
            print ("Os números em ordem decrescente são: ", num3, num1, num2)
if num2 > num1 and num2 > num3:
        if num1 > num3:
            print ("Os números em ordem decrescente são: ", num2, num1, num3)
        if num1 < num3:
            print ("Os números em ordem decrescente são: ", num2, num3, num1)

#num_min = min(num1, num2, num3)
#num_max = max(num1, num2, num3)
#num_mid = (num1 + num2 + num3) - num_min - num_max
#print (f"Os números em ordem decrescente são: {num_max}, {num_mid}, {num_min}")