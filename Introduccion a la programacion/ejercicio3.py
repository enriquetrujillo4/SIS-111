a = int(input("introduce el número: "))
par = 0
impar = 0
while a > 0:
    b = a % 10
    if b % 2 == 0:
        par = par + 1 
    else:
        impar = impar + 1
    a = a // 10 

print("Digitos pares: ",par)
print("Digitos impares: ",impar)