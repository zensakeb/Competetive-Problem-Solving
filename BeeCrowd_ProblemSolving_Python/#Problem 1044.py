#Problem 1044
user_input = input().split()
a = int(user_input[0])
b = int(user_input[1])

if b%a == 0 or a%b == 0:
    print("Sao Multiplos")
else:
    print("Nao sao Multiplos")