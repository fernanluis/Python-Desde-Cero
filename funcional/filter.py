# suponiendo tener una lista de números y desea tomar solamente los números pares
numeros = [1, 2, 3, 4, 5]

def numeros_pares(lista):
    n_pares = []
    for numero in numeros:
        if numero % 2 == 0:
            n_pares.append(numero)
    return n_pares

pares = numeros_pares(numeros)
print(numeros)
print(pares)

# utilizando la función filter que requiere de 2 parámetros, el primero una función y el segundo una lista
numeros = [1, 2, 3, 4, 5]

pares = list(filter(lambda numero : numero % 2 == 0, numeros)) # conversión a unalista

print(numeros)
print(pares)

# otro ejemplo, comprobar si el número es mayor a 2
lista = [1, 2, 3, 4, 5]

pares = list(filter(lambda numero : numero > 2, numeros)) # conversión a unalista

print(numeros)
print(pares)
