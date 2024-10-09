class Coche:
    def __init__(self,marca, modelo, año): 
        self.marca = marca
        self.modelo = modelo 
        self.año = año
        self.encendido = False

    def encender(self):
        if not self.encendido:
            self.encendido = True 
            print(f'el coche {self.marca} {self.modelo} esta encendido')
        else :
            print(f'el cochce {self.marca} {self.modelo} ya esta encendido')
    def apagar(self):
        if self.encendido:
            self.encendido = False 
            print(f'el cocehe {self.marca} {self.modelo} esta apagado')
        else:
            print(f'el coche {self.marca} {self.modelo} esta apagado')
    def mostrar_Estado(self):
        estado = 'encendido' if self.encendido else 'apagado'
        print (f'el coche {self.marca} {self.modelo} esta {estado}')

mi_coche = Coche('toyota', 'corola', 2022)

mi_coche.mostrar_Estado()

mi_coche.encender()
mi_coche.mostrar_Estado()

mi_coche.apagar()
mi_coche.mostrar_Estado()
 