# print e input
# Para comenzar, escribiremos una función que toma un número y lo eleva al cuadrado:
def cuadrado(numero):
    return numero * numero

# Usamos la palabra clave def para indicar que estamos definiendo una función
# tomando una única entrada llamada numero y la palabra clave return para indicar
# cuál debería ser la salida de la función.
# Entonces podemos "llamar" a esta función tal como hemos llamado a otras: usando paréntesis:

for i in range(10):
    print(f"El cuadrado de {i} es {cuadrado(i)}")
