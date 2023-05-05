#Problem 1066
even_count = 0
odd_count = 0
positive = 0
negative = 0

for i in range(5):
    a = int(input())
    if a%2 == 0:
        even_count += 1
    else:
        odd_count += 1
        
    if a>0:
        positive += 1
    elif a<0:
        negative += 1
        
print(even_count,"valor(es) par(es)")
print(odd_count,"valor(es) impar(es)")
print(positive,"valor(es) positivo(s)")
print(negative,"valor(es) negativo(s)")