#Problem 1010
input_1 = input()
input_1 = input_1.split()
units_1 = int(input_1[1])
price_1 = float(input_1[2])


input_2 = input()
input_2 = input_2.split()
units_2 = int(input_2[1])
price_2 = float(input_2[2])

total = (units_1 * price_1) + (units_2 * price_2)

print("VALOR A PAGAR: R$",'%.2f'%total)