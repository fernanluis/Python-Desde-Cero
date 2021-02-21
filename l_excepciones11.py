# Tomaremos dos números enteros del usuario e intentemos dividirlos.

# COMENTAMOS POR LA EXCEPCIÓN MÁS ABAJO
# numero1 = int(input("Ingrese primer numero: "))
# numero2 = int(input("Ingrese segundo numero: "))
# resultado = numero1 / numero2
# print(f"{numero1} / {numero2} = {resultado}")

# Este código puede ofrecer 2 respuestas dependiendo del segundo valor otorgado
# Más precisamente hablando del número cero.

# Podemos lidiar con este desordenado error usando Manejo de Excepciones
# En el siguiente boque de código, intentaremos (try) dividir los dos números,
# excepto (execpt) cuando obtengamos un ZeroDivisionError:

import sys

numero1 = int(input("Ingrese primer numero: "))
numero2 = int(input("Ingrese segundo numero: "))
try:
    resultado = numero1 / numero2
except ZeroDivisionError:
    print("Error: No se puede dividir por 0.")
    # Salir del programa
    sys.exit(1)

print(f"{numero1} / {numero2} = {resultado}")

# Sin embargo aún tenemos errores si el usuario ingresa caracteres que no son
# números.
# Tendremos que controlar también el ingreso de datos al sistema con otro try
