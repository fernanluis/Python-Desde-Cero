class Usuario:

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def registrar(self):
        print(f'El usuario {self.nombre} ha sido registrado')

    def __str__(self):
        return f'La persona se llama {self.nombre} y su edad es {self.edad}'

    def consultar_tipo(self):
        print('Sin especificar')

class Empleado:
    def __init__(self, area_de_trabajo): # conocer el área de trabajo de un vendedor en específico
        self.area_de_trabajo = area_de_trabajo

    def generar_reporte(self):
        print(f'Generando el reporte del empleado del área de {self.area_de_trabajo}')

class Cliente(Usuario): # herencia
    def __init__(self, nombre, edad, numero_compras):
        #self.nombre = nombre reemplazar utilizando herencia
        #self.edad = edad reemplazar utilizando herencia
        #Usuario.__init__(self, nombre, edad) # heredando pero puedo utilizar otra sintaxis
        super().__init__(nombre, edad)# otra forma de escribir la línea de arriba
        self.numero_compras = numero_compras

    def ver_compras(self):
        print(f'El número de compras del cliente {self.nombre} es {self.numero_compras}')

    def consultar_tipo(self):# mismo método que el usuario
        print('El tipo de usuario es: cliente')

cliente = Cliente('Pepe', 34, 56)
cliente.registrar()
cliente.ver_compras()

class Vendedor(Usuario, Empleado):
    def __init__(self, nombre, edad, area_de_trabajo, numero_ventas):
        #self.nombre = nombre reemplazar utilizando herencia
        #self.edad = edad reemplazar utilizando herencia
        #Usuario.__init__(self, nombre, edad) # heredando pero puedo utilizar otra sintaxis
        # super().__init__(nombre, edad)# otra forma de escribir la línea de arriba
        # super hacía referencia a Usuario solamente
        Usuario.__init__(self, nombre, edad)
        Empleado.__init__(self, area_de_trabajo)
        self.numero_ventas = numero_ventas

    def ver_ventas(self):
        print(f'El número de ventas del vendedor {self.nombre} es {self.numero_ventas}')

#    pass  # se escribe pass cuando no hay nada que realizar, no se ejecuta para no dejar una sola línea de una clase.
    def consultar_tipo(self):# mismo método que el usuario
        print('El tipo de usuario es: vendedor')

vendedor = Vendedor('Didi', 33, 'ventas', 45)
vendedor.registrar()
vendedor.ver_ventas()
vendedor.generar_reporte()

usuario = Usuario('Nombre..', 34)
usuario.consultar_tipo()
cliente.consultar_tipo()
vendedor.consultar_tipo()

# crear un método para cualquiera de los 3 objetos.
def mostrar_tipo(objeto):
    objeto.consultar_tipo

mostrar_tipo(vendedor)

for objeto in (usuario, cliente, vendedor):
    objeto.consultar_tipo()
