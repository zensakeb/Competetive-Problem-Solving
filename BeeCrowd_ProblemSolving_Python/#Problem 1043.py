#Problem 1043
user_input = input().split()
a = float(user_input[0])
b = float(user_input[1])
c = float(user_input[2])
if a+b>c and a+c>b and b+c>a:
    print("Perimetro =",a+b+c)
else:
    print("Area =",'%.1f'%(((a+b)/2)*c))