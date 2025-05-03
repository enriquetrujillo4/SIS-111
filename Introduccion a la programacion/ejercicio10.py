
pares=[]
a = int(input("cantidad de números en la lista: "))

for i in range(a):
        num = int(input("introduce el digito: "))
        if (num % 2)== 0:
           pares.append(num)

total = sum(pares)

print("la suma de los numeros pares es: ",total)



