#Problem 1038
s = input().split()
v = int(s[0])
n = int(s[1])
l = [4.00,4.50,5.00,2.00,1.50]
total = 0
if v == 1:
    total = l[0]*n
    print("Total: R$","%.2f"%total)
if v==2:
    total = l[1]*n
    print("Total: R$","%.2f"%total)
if v==3:
    total = l[2]*n
    print("Total: R$","%.2f"%total)
if v==4:
    total = l[3]*n
    print("Total: R$","%.2f"%total)
if v==5:
    total = l[4]*n
    print("Total: R$","%.2f"%total)