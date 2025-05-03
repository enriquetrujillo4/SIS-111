numeros = []
for i in range(4):
    num = int(input("introduzca un número"))
    numeros.append(num)

producto1 = 0

for i in range(4):
    for j in range(i + 1, 4):
        producto = numeros[i] * numeros [j]
        if producto > producto1:
            producto1 = producto

print("el producto mas alto es: ",producto1)