
equipo_a = []
equipo_b = []

for i in range(5):
    a = int(input("introduzca los resultados del equipo a: "))
    equipo_a.append(a)
print(equipo_a)
for i in range(5):
    b = int(input("introduzca los resultados del equipo b: "))
    equipo_b.append(b)
print(equipo_b)
resultado_a = (sum(equipo_a)) / 5
resultado_b = (sum(equipo_b)) / 5

if resultado_a > resultado_b:
    print("El equipo A jugo mejor")
else:
    print("El equipo B jugo mejor")