# Problem 1079
n = int(input())
total = []
for i in range(n):
    sum_a = 0
    count = 0
    a = input().split()
    avg = (float(a[0])*2 + float(a[1])*3 + float(a[2])*5)/10
    total.append(avg)
for i in total:
    print(f'{i:.1f}')