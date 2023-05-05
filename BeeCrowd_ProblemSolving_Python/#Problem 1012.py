#Problem 1012
data = input()
data = data.split()
A = float(data[0])
B = float(data[1])
C = float(data[2])

triangle = 0.5*A*C
circle = 3.14159*(C**2)
trapezium = 0.5*(A+B)*C
square = B**2
rectangle = A*B

print("TRIANGULO:",'%.3f'%triangle)
print("CIRCULO:",'%.3f'%circle)
print("TRAPEZIO:",'%.3f'%trapezium)
print("QUADRADO:",'%.3f'%square)
print("RETANGULO:",'%.3f'%rectangle)