print ("Hello World") # pode remover essa linha

print ("Digite três números para serem colocados em ordem decrescente")
num1 = float(input("Digite seu primeiro número: "))
num2 = float(input("Digite seu segundo número: "))
num3 = float(input("Digite seu terceiro número: "))

num_min = min(num1, num2, num3)
num_max = max(num1, num2, num3)
num_mid = (num1 + num2 + num3) - num_min - num_max # What the f...!

# esta correto, mas tente melhorar essa solução xD
# Por que? Imagine que vc tenha 1 input a mais.. essa solução não vale mais :)
# Imagine então com 200 inputs..
# É mais para treinarmos a logica para problemas maiores que vão aparecer

print (f"Os números em ordem decrescente são: {num_max}, {num_mid}, {num_min}")
