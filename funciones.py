def nombre_funcio1():
    print("salida de funcion1")

def nombre_funcion2():
    print("salida de funcion 2")


def funcion_retorno():
    edad = 18 
    return edad




def obtener_edad():
    edad = int(input("indique su edad "))
    if(edad > 0):
        return edad
    else:
        return 0 
 
def habilitado_brevet(hedad):
    if(hedad == 0 ):
        return "SOLO POSITIVOS"
    if (hedad) >= 18:
        return "verdadero "
    else:
        return"falso"


def calcular_descuento_producto():
    precio_original = 100 
    descuento = 20 
    precio_descuento = (precio_original * descuento/ 100)
    precion_final = precio_original - precio_descuento
    return precion_final

def calcular_descuento_procunto_mejorado(precio_original, descuento):
    precio_descuento = (precio_original * descuento)/100
    precio_final = precio_original - precio_descuento
    return precio_final 


def calcular_descuento_preducto_mejorado_x2():
    return precio_original - (precio_original * descuento)/100
    
def calcular_descuento_preducto_mejorado_x3():
    return precio_original * (1 - descuento / 100)


#edad minima para votar

def edad_minima_votar():
    print("la edad minima es 18 años")


# numero mayor entre dos numeros

def mayor_dos_num(numA, numB):
    if(numA == numB): "iguales"

    if(numA > numB):
        return numA
    else:
        return numB

def mayor_dos_num_mejorado(numA, numB):
    if(numA == numB): return "iguales"

    return numA if (numA > numB) else numB


def recorrer_digitos(num):
    while(num > 0):
        dig = num % 10
        print(dig)
        num = num // 10

# Par/Impar de los dig de un num 

def par_impar_dig(num):
    while(num > 0):
        dig = num % 10 
        print(dig)

        var_temp = "par" if(dig% 2 == 0 ) else "impar"
        print(var_temp)

        num = num // 10 

def suma_dig_num(num):
    suma = 0
    while(num % 10):
        dig = num % 10 
        suma = suma + dig 
        num = num // 10 
    return suma

var_suma = suma_dig_num(78234)
print(var_suma)

    



var_numA = int(input("ingrese el numero a "))
var_numB = int(input("ingrese el numero b"))
var_num_mayor = mayor_dos_num(var_numA, var_numB)
print(var_num_mayor)
    


#var_precio_f = calcular_descuento_producto()
#print(var_precio_f) 

precio_original =int(input("ingrese el precio del producto: "))
descuento = int(input("ingrese el porcentaje de descuento"))
var_precio_ff = calcular_descuento_procunto_mejorado(precio_original, descuento)



#salida

var_salida = nombre_funcion2()
print(var_salida)
