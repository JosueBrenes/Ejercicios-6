# = Función sin retorno (Retorno None)

def sumar (x,y): 
    resultado = x + y
    print("La suma es: ", resultado)

def restar (x,y):
    resultado = x - y
    print("La resta es:", resultado)

def multiplicacion (x,y):
    resultado = x * y
    print("La multiplicación es: ", resultado)

def dividir (x,y):
    resultado = x / y
    print("La división es: ", resultado)

numero1 = int(input("Primer número: "))
numero2 = int(input("Segundo número: "))

sumar(numero1,numero2)
restar(numero1,numero2)
multiplicacion(numero1,numero2)
dividir(numero1,numero2)