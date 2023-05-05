#Problem 2592
while True:
    user_input = int(input())
    if user_input == 0:
        break
    else:
        count = 0
        result = []
        for i in range(1,user_input+1):
            result.append(i)

        while True:
            num_input = input()
            num_list = num_input.split()
            int_list = []

            for i in num_list:
                int_list.append(int(i))

            count += 1

            if int_list == result:
                print(count)
                count = 0
                break