#Problem 1042
user_input = input().split()
acc_order = []
for i in user_input:
    acc_order.append(int(i))
acc_order.sort()

print(*acc_order, sep = "\n")
print()
print(f'\n'.join(user_input))
