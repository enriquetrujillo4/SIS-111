
b = int(input("introduce el número: "))

lista_b = [int(d) for d in str(b)]

palin = []
while b > 0:
    c = b % 10
    palin.append(c)
    b = b // 10 

if palin == lista_b:
    print("Es un palindromo")
else:
    print("No es un palindromo")

