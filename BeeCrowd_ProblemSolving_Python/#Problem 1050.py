#Problem 1050
result = {"61":"Brasilia","71":"Salvador","11":"Sao Paulo","21":"Rio de Janeiro","32":"Juiz de Fora","19":"Campinas","27":"Vitoria","31":"Belo Horizonte"}
user = input()

if user in result.keys():
    for k,v in result.items():
        if user == k:
            print(v)
else:
    print("DDD nao cadastrado")