lista = []
tamaño_lista = int(input("cuanto digitos tiene la lista: "))
digito = int(input("Que digito desea buscar: "))
verdad = 0
for i in range(tamaño_lista):
    num = int(input("introduzca un número: "))
    if num == digito:
        verdad = verdad + 1
    lista.append(num)

print(lista)
if verdad == 1:
    print("número encontrado")
else:
    print("número no encontrado")