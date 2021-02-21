# Clases: ya hemos visto algunos tipos diferentes de variables en Python,
# pero ¿qué pasa si queremos crear nuestro propio tipo?
# Una clase de Python es esencialmente una plantilla para un nuevo
# tipo de objeto que puede almacenar información y realizar acciones.
# Aquí hay una clase que define un punto bidimensional:

#    class Punto():
    # Un método que define como crear un punto:
#        def __init__(self, x, y):
#            self.x = x
#            self.y = y

# Ten en cuenta que en el código anterior, usamos la palabra clave self
# para representar el objeto con el que estamos trabajando actualmente.
# self debería ser el primer argumento para cualquier método dentro de
# una clase Python.

# una clase es como un formulario o cuestionario.
# Una instancia es como un formulario que se ha llenado con información.

# A continuación creamos un objeto a partir de la clase de arriba.

#    p = Punto(2, 8) # INSTANCIA
#        print(p.x)
#        print(p.y)

# Ahora, veamos un ejemplo más interesante en el que en lugar de almacenar solo las
# coordenadas de un punto, creamos una clase que representa el vuelo de una aerolínea:


#        class Vuelo():
        # Metodo para crear un nuevo vuelo con una capacidad dada
#            def __init__(self, capacidad):
#                self.capacidad = capacidad
#                self.pasajeros = []
        # Metodo para agregar un pasajero al vuelo:
#            def agregar_pasajero(self, nombre):
#                self.pasajeros.append(nombre)

# Sin embargo, esta clase tiene fallas porque aunque establezcamos una capacidad, aún podríamos
# agregar demasiados pasajeros. Modifiquemos para que antes de agregar un pasajero, verifiquemos si
# hay espacio en el vuelo:

class Vuelo():
# Metodo para crear un nuevo vuelo con una capacidad dada
    def __init__(self, capacidad):
        self.capacidad = capacidad
        self.pasajeros = []
# Metodo para agregar un pasajero al vuelo:
    def agregar_pasajero(self, nombre):
        if not self.asientos_disponibles(): # Esto funciona porque en Python, el número 0 se puede interpretar como False, y también podemos usar la palabra clave not para significar lo opuesto a la siguiente declaración, por lo que not True es False y not False es True. Por lo tanto, si asientos_disponibles devuelve 0, toda la expresión se evaluará como True
            return False
        self.pasajeros.append(nombre)
        return True
# Metodo para retornar el numero de asientos disponibles
    def asientos_disponibles(self):
        return self.capacidad - len(self.pasajeros)

# Instanciando los objetos

# Ahora, probemos la clase que hemos creado creando instancias de algunos objetos:
# Crear un nuevo vuelo con hasta 3 personas
unVuelo = Vuelo(3)
# Crear una lista de personas
personas = ["Harry", "Ron", "Hermione", "Ginny"]
# Intentar agregar cada persona de la lista al vuelo
for unaPersona in personas:
    if unVuelo.agregar_pasajero(unaPersona):
        print(f"Agregado {unaPersona} al vuelo satisfactoriamente")
    else:
        print(f"No hay asientos disponibles para {unaPersona}")
