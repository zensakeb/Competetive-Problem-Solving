#Problem 1040
user_input = input().split()
a1 = float(user_input[0])
a2 = float(user_input[1])
a3 = float(user_input[2])
a4 = float(user_input[3])

media = (a1*2+a2*3+a3*4+a4)/10
print("Media:",'%.1f'%media)

if media>=7.0:
    print("Aluno aprovado.")
elif media<=6.9 and media>=5.0:
    print("Aluno em exame.")
    next_input = float(input())
    media = (media + next_input)/2
    print("Nota do exame:",next_input)
    if media >= 5.0:
        print("Aluno aprovado.")
    else:
        print("Aluno reprovado.")
    print("Media final:",media)
        
else:
    print("Aluno reprovado.")