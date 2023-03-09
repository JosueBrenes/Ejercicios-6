# = Función que recibe un numero e imprime su equivalente en binario
def binario(numero):
    numeroBinario = bin(numero)
    print("El",numero, "en binario es:",numeroBinario[2:]) # = El [2:] es para recorte en el segundo caracter 

# = Función que recibe un numero e imprime su equivalente en octal
def octal(numero):
    numeroOctal = oct(numero)
    return numeroOctal

# = Función que recibe un numero e imprime su equivalente en hexadecimal
def hexadecimal(numero):
    numeroHexa = hex(numero)
    return numeroHexa

# = Funcion que recibe dos numeros y eleva el primer numero a la pontencia del segundo numero
def pontencia(numero, exponente):
    return numero ** exponente 

numero = int(input("Digite un número: ")) # = Solicitamos al usuario que digite un número entero
binario(numero) 

print("El",numero, "en hexadecimal es:", octal(numero)[2:]) # = Imprimimos su equivalente en octal
print("El",numero, "en hexadecimal es:", hexadecimal(numero)[2:]) # = Imprimimos su equivalente en hexadecinal

exponente = int(input("Digite otro número entero: "))
print(numero, "elevado a", exponente, "es", pontencia(numero, exponente))