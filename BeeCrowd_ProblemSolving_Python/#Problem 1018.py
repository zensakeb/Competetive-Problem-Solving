#Problem 1018
user_input = int(input())
bank_notes = [100,50,20,10,5,2,1]
note_list = []
if user_input>0 and user_input<1000000:
    print(user_input)
    while True:
        notes = int()
        remain = user_input
        for i in bank_notes:
            if i<= remain:
                notes = remain//i
                remain = remain % i
            else:
                notes = 0
                
            print(notes,"nota(s) de R$",str(i)+",00")
        break
    