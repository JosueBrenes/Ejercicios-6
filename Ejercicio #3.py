# = Función con retorno

def sumar (x,y): 
    resultado = x + y
    return resultado

def restar (x,y):
    resultado = x - y
    return resultado

def multiplicacion (x,y):
    resultado = x * y
    return resultado

def dividir (x,y):
    resultado = x / y
    return resultado

numero1 = int(input("Primer número: "))
numero2 = int(input("Segundo número: "))

resultado = sumar(numero1,numero2)

print("La suma es: ", resultado)
print("La resta es:", restar(numero1,numero2))
print("La multiplicación es: ", multiplicacion(numero1,numero2))
print("La división es: ", dividir(numero1,numero2))