#Problem 1051
user_input  = float(input())
tax = 0
if user_input>= 0.00 and user_input<= 2000.00:
    print("Isento")
elif user_input>=2000.01 and user_input<=3000.00:
    tax = (user_input-2000)*0.08
    print("R$","%.2f"%tax)
elif user_input>=3000.01 and user_input<= 4500.00:
    tax = 1000*0.08+(user_input-3000)*0.18
    print("R$","%.2f"%tax)
else:
    tax = 1000*0.08+1500*0.18+(user_input-4500)*0.28
    print("R$","%.2f"%tax)