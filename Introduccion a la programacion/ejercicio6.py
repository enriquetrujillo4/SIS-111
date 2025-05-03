meta = int (input("meta$"))

dias = 0
ahorro = 5
total = 5

while total < meta:
    dias = dias + 1
    total = total + ahorro
    ahorro = ahorro + 2

print("los dias necesarios son: ",dias)


