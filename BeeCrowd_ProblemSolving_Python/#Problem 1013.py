#Problem 1013
import math
user_input = input()
user_input = user_input.split()
a = int(user_input[0])
b = int(user_input[1])
c = int(user_input[2])

tot = (a + b + abs(a-b))/2
maior = (tot + c + abs(tot-c))/2

print(int(maior),"eh o maior")