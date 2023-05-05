#Problem 1036
user_input = input().split()
a = float(user_input[0])
b = float(user_input[1])
c = float(user_input[2])

if a != 0:

    r1 = ((-1*b) + ((b**2) - (4*a*c))**0.5)/(2*a)
    r2 = ((-1*b) - ((b**2) - (4*a*c))**0.5)/(2*a)

    if (type(r1) == float) and (type(r2) == float):
        print("R1 =","%.5f"%r1)
        print("R2 =","%.5f"%r2)
    else:
        print("Impossivel calcular")
else:
    print("Impossivel calcular")