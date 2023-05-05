#Problem 1070
x = int(input())
j = 2
if x % 2 != 0:
    print(x)
    for i in range(5):
        print(x+j)
        j += 2
else:
    for i in range(6):
        print(x-1+j)
        j += 2