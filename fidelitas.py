menu= int(input("Bienvenido a la calculadora Fidelitas, seleccione la operacion que desea realizar:1. Sumar,2. Restar,3. Multiplicar,4. Dividir)"))

def sumar(x, y):
    resultado = x + y
    return resultado

def restar(x, y):
    return x - y

def multiplicar(x, y):
    resultado = x * y
    return resultado

def dividir(x, y):
    resultado = x / y
    return resultado


# Proceso inicial
a = int(input("Primer número: "))
b = int(input("Segundo número: "))

if menu == 1:
    resultado = sumar(a, b)
    print("La suma es:", resultado)
elif menu == 2:
    resultado = restar(a, b)
    print("La resta es:", resultado)
elif menu == 3:
    resultado = multiplicar(a, b)
    print("La multiplicación es:", resultado)
elif menu == 4:
    resultado = dividir(a, b)
    print("La división es:", resultado)