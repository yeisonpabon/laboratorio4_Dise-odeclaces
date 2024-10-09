class Persona:
    def __init__(self,nombre,edad):
        self.nombre = nombre
        self.edad = edad
        self.estado = 'despierto'

    def dormir(self):
        self.estado = 'dormido'

    def despierto(self):
        self.estado = 'despierto'

    def mostrar_estado(self):
        print (f'{self.nombre} tiene {self.edad} años y esta {self.estado}')

person = Persona('yeison', 22)
person.dormir()
person.mostrar_estado()
person.despierto()
person.mostrar_estado()