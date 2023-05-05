#Problem 1259
num_times = int(input())
if num_times > 1 and num_times <= 10**5:
    even_list=[]
    odd_list = []
    for i in range(num_times):
        user_num = int(input())
        if user_num%2 == 0:
            even_list.append(user_num)
        else:
            odd_list.append(user_num)
            
    even_list.sort()
    odd_list.sort(reverse=True)
    result = even_list + odd_list
    for i in result:
        print(i)