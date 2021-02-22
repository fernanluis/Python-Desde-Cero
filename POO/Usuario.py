class Usuario:

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def registrar(self):
        print(f'El usuario {self.nombre} ha sido registrado')

    def __str__(self):
        return f'La persona se llama {self.nombre} y su edad es {self.edad}'

class Cliente(Usuario): # herencia
    def __init__(self, nombre, edad, numero_compras):
        #self.nombre = nombre reemplazar utilizando herencia
        #self.edad = edad reemplazar utilizando herencia
        #Usuario.__init__(self, nombre, edad) # heredando pero puedo utilizar otra sintaxis
        super().__init__(nombre, edad)# otra forma de escribir la línea de arriba
        self.numero_compras = numero_compras

    def ver_compras(self):
        print(f'El número de compras del cliente {self.nombre} es {self.numero_compras}')


cliente = Cliente('Pepe', 34, 56)
cliente.registrar()
cliente.ver_compras()

class Vendedor(Usuario):
    def __init__(self, nombre, edad, numero_ventas):
        #self.nombre = nombre reemplazar utilizando herencia
        #self.edad = edad reemplazar utilizando herencia
        #Usuario.__init__(self, nombre, edad) # heredando pero puedo utilizar otra sintaxis
        super().__init__(nombre, edad)# otra forma de escribir la línea de arriba
        self.numero_ventas = numero_ventas

    def ver_ventas(self):
        print(f'El número de ventas del vendedor {self.nombre} es {self.numero_ventas}')


#    pass  # se escribe pass cuando no hay nada que realizar, no se ejecuta para no dejar una sola línea de una clase.



vendedor = Vendedor('Didi', 33, 45)
vendedor.registrar()
vendedor.ver_ventas()
