#Problem 1064
pos_num = 0
sum_num = 0
for i in range(6):
    user_input = float(input())
    if user_input>0:
        pos_num += 1
        sum_num += user_input
        
print(f'{pos_num} valores positivos\n{(sum_num/pos_num):.1f}')
