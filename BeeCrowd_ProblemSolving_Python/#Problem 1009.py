#Problem 1009
name = input()
salary  = float(input())
sales = float(input())

bonus = salary + (sales * 0.15)

print("TOTAL = R$",'%.2f'%bonus)