print ("Hello World")
product_one = float(input("Digite o valor do produto 1: "))
product_two = float(input("Digite o valor do produto 2: "))
product_three = float(input("Digite o valor do produto 3: "))

resp = min(product_one, product_two, product_three)
if resp == product_one:
    print ("O produto a ser comprado, deverá ser o produto 1")
elif resp == product_two:
    print ("O produto a ser comprado, deverá ser o produto 2")
else:
    print ("O produto a ser comprado, deverá ser o produto 3")