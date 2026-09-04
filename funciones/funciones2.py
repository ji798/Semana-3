#Sumar 2 numeros

def sumar(numero1 , numero2):

    return numero1 + numero2

suma = sumar(15, 17)
print(suma)

def restar(num1 = 0 , num2 = 0):
    return num1 - num2

def multiplicar(numero1 = 0 , numero2 = 0):
    return numero1 * numero2

def dividir(numero1 = 0 , numero2 = 0):
    try:
        return numero1 / numero2
    except ZeroDivisionError:
        return "Error: División por cero no permitida"

resta = restar(4, 2)
print(resta)

resta = restar(num2= 6, num1=2)
print(resta)

producto = multiplicar(3, 4)
print(producto)

cociente = dividir(10, 2)
print(cociente)

cociente = dividir(10, 0)
print(cociente)