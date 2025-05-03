numeros = []
lista = []

for i in range(4):
    a = int(input("Introduzca el número: "))
    numeros.append(a)

for i in range(4):
    for j in range(i + 1, 4):

        lista_2 = (numeros[i], numeros[j])

        lista.append( lista_2)

print(lista)
        


        

