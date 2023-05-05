#Problem 1071
x = int(input())
y = int(input())
total = 0
if x>y:
    for i in range(y+1,x):
        if i % 2 != 0:
            total += i
elif y>x:
    for i in range(x+1,y):
        if i % 2 != 0:
            total += i
else:
    total = 0
print(total)