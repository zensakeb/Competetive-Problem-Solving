#Problem 1074

result = []
n = int(input())
for i in range(n):
    num = int(input())
    string = ''
    if num >0:
        if num % 2 == 0:
            string = 'EVEN POSITIVE'
        else:
            string = 'ODD POSITIVE'
    elif num<0:
        if num % 2 == 0:
            string = 'EVEN NEGATIVE'
        else:
            string = 'ODD NEGATIVE'
    else:
        string = 'NULL'
        
    result.append(string)
for i in result:
    print(i)