#Problem 2508
import sys

PT = {1:['A','J','S'], 2:['B','K','T'], 3:['C','L','U'], 4:['D','M','V'], 5:['E','N','W'], 6:['F','O','X'], 7:['G','P','Y'], 8:['H','Q','Z'], 9:['I','R']}

for N in sys.stdin:
 
    N=N.upper()
    total=0

    if len(N)<=100:
        for i in N:
            if i=='Ç' or i=='ç':
                i='C'
            for k,v in PT.items():
                for z in v:
                    if z==i:
                        total+=int(k)
        total=str(total)

        total2=0
        for i in total:
            total2+=int(i)

        total2=str(total2)
        total3=0
        for i in total2:
            total3+=int(i)
        print(total3)