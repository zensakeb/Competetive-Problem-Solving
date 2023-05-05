#Problem 1019
n = int(input())
h = n//3600
remain = n%3600
m = remain//60
s = remain%60

print(str(h)+":"+str(m)+":"+str(s))