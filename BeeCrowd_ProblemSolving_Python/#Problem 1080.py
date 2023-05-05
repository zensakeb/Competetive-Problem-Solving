#Problem 1080
grt_num = 0
pos = 1
for i in range(1,101):
    user_input = int(input())
    if user_input>grt_num:
        grt_num = user_input
        pos = i
        
print(f'{grt_num}\n{pos}')