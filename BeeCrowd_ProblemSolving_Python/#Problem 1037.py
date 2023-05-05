#Problem 1037
user_input = float(input())
result = ["[0,25]","(25,50]","(50,75]","(75,100]"]
if user_input<0 or user_input>100:
    print("Fora de intervalo")
else:
    if user_input>=0 and user_input<=25:
        print("Intervalo",result[0])
    elif user_input>25 and user_input<=50:
        print("Intervalo",result[1])
    elif user_input>50 and user_input<=75:
        print("Intervalo",result[2])
    else:
        print("Intervalo",result[3])