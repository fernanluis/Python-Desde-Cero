class Persona:

    def __init__(self, nombre, edad): # método inicializador con 2 parámetros que hace referencia a la propa clase y parámetro para construir los atributos de la clase
        #self.arg = arg # self seguido el atributo
        self.nombre = nombre
        self.edad = edad
    # a continuación se crearán métodos
    def caminar(self):
        print(f'{self.nombre} está caminando') # f detecta el atributo nombre. y siempre se utiliza self.

    def correr(self):
        print(f'{self.nombre} esta corriendo')

    # para crear una instancia de la clase se crea un método llamado str definido en python
    # para cuando se muestre toda la clase persona retorna una cadena de texto.
    def __str__(self):
        return f'La persona se llama {self.nombre} y su edad es {self.edad}'

# instancia de la clase

persona = Persona('Luis', 34)
print(persona)
persona.caminar()
persona.correr()
print(persona.nombre)
print(persona.edad)
persona2 = Persona('Didi', 34)
persona3 = Persona('Ana Clara', 4)
persona2.caminar()
persona2.correr()
persona3.caminar()
persona3.correr()
