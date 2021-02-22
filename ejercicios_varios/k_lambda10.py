# Programación funcional:
# Python no sabe cómo comparar dos diccionarios para comprobar
# si uno es menor que otro.
# Incluímos un argumento key

personas = [
    {"nombre": "Harry", "casa": "Griffindor"},
    {"nombre": "Cho", "casa": "Ravenclaw"},
    {"nombre": "Draco", "casa": "Slytherin"}
]

def f(unaPersona):
    return unaPersona["nombre"]

personas.sort(key=f)

print(personas)

# Si bien esto funciona, hemos tenido que escribir una función completa
# que sólo usamos una vez.Podemos hacer que nuestro código sea más legible
# mediante el uso de una función lambda

personas = [
    {"nombre": "Harry", "casa": "Griffindor"},
    {"nombre": "Cho", "casa": "Ravenclaw"},
    {"nombre": "Draco", "casa": "Slytherin"}
]

personas.sort(key=lambda unaPersona: unaPersona["nombre"])

print(personas)
