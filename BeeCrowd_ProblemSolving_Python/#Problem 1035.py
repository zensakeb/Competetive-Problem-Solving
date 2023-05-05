#Problem 1035
user_input = input().split()
a = int(user_input[0])
b = int(user_input[1])
c = int(user_input[2])
d = int(user_input[3])
if a%2==0:
    if c>=0 and d>=0:   
        if b>c and d>a:
            if (c+d)>(a+b):
                print("Valores aceitos")
            else:
                print("Valores nao aceitos")
        else:
            print("Valores nao aceitos")
    else:
        print("Valores nao aceitos")
else:
    print("Valores nao aceitos")