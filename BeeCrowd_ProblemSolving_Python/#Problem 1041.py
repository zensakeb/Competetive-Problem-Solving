#Problem 1041
user_input = input().split()
x = float(user_input[0])
y = float(user_input[1])
if x==0.0 and y==0.0:
    print("Origem")
elif y == 0:
    print("Eixo X")
elif x == 0:
    print("Eixo Y")
elif x>0 and y>0:
    print("Q1")
elif x<0 and y>0:
    print("Q2")
elif x<0 and y<0:
    print("Q3")
elif x>0 and y<0:
    print("Q4")