#Problem 1168
n_v = {1:2,2:5,3:5,4:4,5:5,6:6,7:3,8:7,9:6,0:6}
num = int(input())
if num>=1 and num<=2000:
    result = []
    for i in range(num):
        str_input = input()
        count = 0
        for j in str_input:
            for k,v in n_v.items():
                if int(j)==k:
                    count += v
        result.append(count)
            
    for i in result:
        print(i,"leds")