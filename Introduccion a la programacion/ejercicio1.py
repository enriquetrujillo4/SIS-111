cantidad_intentos = 0
verdad = 0
a = int(input("introduzca un número: "))
while cantidad_intentos < 4:
    
    b = int(input("introduzca un número: "))
    if a > b:
        verdad = verdad +1
    else:
        verdad = verdad - 1 
    cantidad_intentos = cantidad_intentos + 1

if verdad < 0:
    print("orden ascendente")
else:
    print("orden descendente")
