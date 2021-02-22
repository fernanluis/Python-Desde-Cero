# cadena de caracteres
# -> class str
mensaje = 'Esto es un texto de prueba'
print(type(mensaje))
# en Python no existe el tipo caracter, solo lo representa como string
numero_5 = '5'
print(type(numero_5))

# Números
# -> class int
numero_5 = -5
numero_5 = 5
print(type(numero_5))
print(type(numero_5))

# Flotantes o decimales
n_decimal = 2.4
print(type(n_decimal))

suma_decimal = 2.4 + 3.2
print(type(suma_decimal))

calculo = 2.4 / 3.2
print(type(calculo))

# números complejos compuesto por una parte real y una parte imaginaria
# -> class complex
complejo = 2 + 2j
print(type(complejo))
# en python cada parte de un tipo de dato complejo está representado por un tipo float.
complejo = 2 + 2j
print(type(complejo.real)) # imprimiendo la parte real
print(type(complejo.imag)) # imprimiendo la parte imaginaria

#Booleanos
#class bool
nivel_dificil = False
curso_aprobado = True
print(type(curso_aprobado))
print(type(nivel_dificil))

suma = 4 + 5 == 11
print(type(suma))
