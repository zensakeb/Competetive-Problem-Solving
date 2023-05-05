#Problem 1072
n_in = 0
n_out = 0
n = int(input())
for i in range(n):
    x = int(input())
    if x>=10 and x<=20:
        n_in += 1
    else:
        n_out += 1
        
print(f'{n_in} in\n{n_out} out')