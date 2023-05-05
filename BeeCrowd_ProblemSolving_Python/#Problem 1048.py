#Problem 1048
user = float(input())
if user>0 and user<=400.00:
    inc = 15
    print(f"Novo salario: {'%.2f'%(user + (user*0.15))}")
    print(f"Reajuste ganho: {'%.2f'%(user*0.15)}")
    print(f"Em percentual: {inc} %")
    
elif user>400.00 and user<=800.00:
    inc = 12
    print(f"Novo salario: {'%.2f'%(user + (user*0.12))}")
    print(f"Reajuste ganho: {'%.2f'%(user*0.12)}")
    print(f"Em percentual: {inc} %")
    
elif user>800.00 and user<=1200.00:
    inc = 10
    print(f"Novo salario: {'%.2f'%(user + (user*0.1))}")
    print(f"Reajuste ganho: {'%.2f'%(user*0.1)}")
    print(f"Em percentual: {inc} %")
    
elif user>1200.00 and user<=2000.00:
    inc = 7
    print(f"Novo salario: {'%.2f'%(user + (user*0.07))}")
    print(f"Reajuste ganho: {'%.2f'%(user*0.07)}")
    print(f"Em percentual: {inc} %")
    
else:
    inc = 4
    print(f"Novo salario: {'%.2f'%(user + (user*0.04))}")
    print(f"Reajuste ganho: {'%.2f'%(user*0.04)}")
    print(f"Em percentual: {inc} %")