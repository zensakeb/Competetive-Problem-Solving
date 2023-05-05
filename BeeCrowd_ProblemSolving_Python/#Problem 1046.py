#Problem 1046
user_input = input().split()
a = int(user_input[0])
b = int(user_input[1])

if a==b:
    print("O JOGO DUROU 24 HORA(S)")
elif b>a:
    print(f"O JOGO DUROU {b-a} HORA(S)")
else:
    print(f"O JOGO DUROU {(24-a)+b} HORA(S)")