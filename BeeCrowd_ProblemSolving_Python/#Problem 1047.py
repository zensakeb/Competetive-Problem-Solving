#Problem 1047
user_input = input().split()
a = int(user_input[0])
a1 = int(user_input[1]) 
b = int(user_input[2])
b1 = int(user_input[3])

if a == a1 and b == b1 and a == b:
    print("O JOGO DUROU 24 HORA(S) E 0 MINUTO(S)")
elif b>=a and b1>a1:
    print(f"O JOGO DUROU {b-a} HORA(S) E {b1-a1} MINUTO(S)")
elif b>a and a1>b1:
    print(f"O JOGO DUROU {b-a-1} HORA(S) E {60-(a1-b1)} MINUTO(S)")
elif a>b and b1>a1:
    print(f"O JOGO DUROU {24-(a-b)} HORA(S) E {b1-a1} MINUTO(S)")
elif a>=b and a1>b1:
    print(f"O JOGO DUROU {23-(a-b)} HORA(S) E {60-(a1-b1)} MINUTO(S)")