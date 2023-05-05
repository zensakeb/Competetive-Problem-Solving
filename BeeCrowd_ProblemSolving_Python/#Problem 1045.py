#Problem 1045
new_input = input().split()
user_input = []
for i in new_input:
    user_input.append(float(i))
user_input.sort(reverse=True)
a = user_input[0]
b = user_input[1]
c = user_input[2]

if a>=(b+c):
    print("NAO FORMA TRIANGULO")
elif a**2 == (b**2 + c**2):
    print("TRIANGULO RETANGULO")
elif a**2 > (b**2 + c**2):
    print("TRIANGULO OBTUSANGULO")
elif a**2 < (b**2 + c**2):
    print("TRIANGULO ACUTANGULO")
if a==b and b==c:
    print("TRIANGULO EQUILATERO")
elif (a==b and a!=c) or (c==b and a!=c) or (a==c and a!=b):
    print("TRIANGULO ISOSCELES")