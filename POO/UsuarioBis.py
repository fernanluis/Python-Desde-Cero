# encapsulamiento

class Usuario:

    def __init__(self):
        self.__nombre = 'Ana' # __ indica que son privados
        self.__edad = 4

    # getters
    def getNombre(self):
        return self.__nombre
    def getEdad(self):
        return self.__edad

    # setters
    def setNombre(self, nombre):
        if nombre == 'Ana':
            self.__nombre = nombre
        else:
            return 'No puede asignar ese nombre'

    def setEdad(self, edad):
        if edad == 4:
            self.__edad = edad
        else:
            return 'No puede asignar esa edad'

    def __registrar(self): # __ inica que son privados
        print(f'El usuario {self.__nombre} ha sido registrado')

    def __str__(self):
        return f'La persona se llama {self.__nombre} y su edad es {self.__edad}'

    def consultar_tipo(self):
        self.__registrar()
        print('Sin especificar')

# usuario = Usuario("Luis", 34)
usuario = Usuario()
# print(usuario.nombre) los atributos de la clase son privados (__)
# print(usuario.edad) los atributos de la clase son privados (__)
# usuario.registrar método privado
usuario.consultar_tipo()
print(usuario.getNombre())
print(usuario.getEdad())
print(usuario.setNombre('Luis'))
print(usuario.setEdad(34))
