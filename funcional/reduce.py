#* import functools # el módulo functools contiene a la función reduce()
# otra forma de importar es:
from functools import reduce

lista = [2, 4, 6, 8, 10]
def unir(x, y):
    return x + y
#1ro
#x = 2
#y = 4
#resultado = 6
#2do
#x = 6
#y = 6
#resultado = 12
#3ro
#x = 12
#y = 8
#resultado = 20

#4to
#x = 20
#y = 10
#resultado = 30

resultado = reduce(unir,lista)
#* functools.reduce(funcion, lista) # parámetro función y lista de elementos.

print(resultado)

# utilizando lambda
lista = [2, 4, 6, 8, 10]
resultado1 = lambda x, y: x + y

resultado = reduce(resultado1,lista)
print(resultado)
