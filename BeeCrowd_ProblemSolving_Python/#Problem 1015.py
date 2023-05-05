#Problem 1015
user_input1 = input()
user_input2 = input()

user_input1 = user_input1.split()
user_input2 = user_input2.split()

x1=float(user_input1[0])
y1=float(user_input1[1])
x2=float(user_input2[0])
y2=float(user_input2[1])

distance = ((x2 - x1)**2 + (y2 - y1)**2)**0.5

print("%.4f"%distance)