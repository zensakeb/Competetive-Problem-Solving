#Problem 1020
n = int(input())
y = n//365
r = n%365
m = r//30
d = r%30

print(y,"ano(s)")
print(m,"mes(es)")
print(d,"dia(s)")