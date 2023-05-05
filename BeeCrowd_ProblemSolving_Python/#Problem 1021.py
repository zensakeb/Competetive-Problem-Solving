#Problem 1021
user_input = float(input())
bank_notes = [100,50,20,10,5,2]
bank_coins = ["0.50","0.25","0.10","0.05","0.01"]
note_list = []
coin_list = []
if user_input>=0 and user_input<=1000000.00:
    user_input = str(user_input)
    user_input = user_input.split(".")
    print("NOTAS:")
    while True:
        notes = int()
        remain = int(user_input[0])
        if remain != 1:
            for i in bank_notes:
                if i<= remain:
                    notes = remain//i
                    remain = remain % i
                else:
                    notes = 0
                    
                print(notes,"nota(s) de R$",str(i)+".00")
            break
    print("MOEDAS:")
    if remain == 1:
        print(1,"moeda(s) de R$","1.00")
    else:
        print(0,"moeda(s) de R$","1.00")
    while True:
        change = int()
        remain = (int(user_input[1]))
        for i in bank_coins:
            a = int(float(i)*100)
            if a<= remain:
                change = remain//a
                remain = remain%a
            else:
                change = 0
                
            print(change,"moeda(s) de R$",i)
        break