a = int(input("ingresa el número: "))
primo = 0
for i in range(2, a):
    if a % i == 0:
        primo = primo + 1
        break

if primo == 1:
    print("No es primo")
else:
    print("Es primo")