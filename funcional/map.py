numeros = [1, 2, 3, 4, 5] # crear una lista de números

def duplicar(lista): # función con parámetro lista
    numeros_duplicados = [] # crear una nueva lista
    for numero in numeros: # pasar c/u de la lista números a la nueva lista con los valores duplicados
        numeros_duplicados.append(numero*2)

    return numeros_duplicados

duplicados = duplicar(numeros)
print(duplicados)

# para evitar el ciclo for es posibe utilizarla función map()con 2 parámetros, el primero será una función y el segundo, una lista.
numeros = [1, 2, 3, 4, 5]
def duplicar (numero):
    return numero * 2

numero_duplicado2 = list(map(duplicar, numeros)) # conversión a lista
print(numero_duplicado2)

# reemplazo de la función por una función lambda
numeros = [1, 2, 3, 4, 5]
duplicar = lambda numero : numero * 2

numero_duplicado2 = list(map(duplicar, numeros)) # conversión a lista
print(numero_duplicado2)

# agreagar 2 listas y realizar conversión entre ellas con el objetivo de que devuelva una lista totalmente distinta.
#la función map() devuelve una lista diferente.
lista1 = [1, 2, 3, 4, 5]
lista2 = [1, 1, 1, 1, 1]

suma = list(map(lambda l1, l2 : l1 + l2, lista1, lista2 ))
print(suma)
