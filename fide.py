import array
def suma_mayores_de_18(a,b):
    return a + b
def resta_mayores_de_18(a,b):
    return a - b
# Definir la cantidad de números a ingresar
tamano = int(input("Ingrese la cantidad de números que desea ingresar: "))
 
# Crear un arreglo de enteros
numeros = array.array('i')
 
# Ingreso de datos por el usuario
for i in range(tamano):
    valor = int(input("Ingrese el número # "))
    numeros.append(valor)
 
# Mostrar el contenido del arreglo
print("El contenido del arreglo es:")
for n in numeros:
    print(n)
 
# Capturar los valores mayores de 18
print("Los mayopres de 18 son:")
for n in numeros:
     if n > 18:
           print (n)
 
# Sumar valores mayores de 18
suma = []
for n in numeros:
     if n > 18:
         suma.append(n)
print("La suma de los mayores de 18 es:", sum(suma) )
 
# REsta valores mayores de 18   resta = x - resta
resta = []
for n in numeros:
     if n > 18:
           resta.append(n)
print("La resta de los mayores de 18 es:", reduce  )