print ("Hello World")
print ("Digite três números para serem colocados em ordem decrescente")
num1 = float(input("Digite seu primeiro número: "))
num2 = float(input("Digite seu segundo número: "))
num3 = float(input("Digite seu terceiro número: "))

num_min = min(num1, num2, num3)
num_max = max(num1, num2, num3)
num_mid = (num1 + num2 + num3) - num_min - num_max

print (f"Os números em ordem decrescente são: {num_max}, {num_mid}, {num_min}")