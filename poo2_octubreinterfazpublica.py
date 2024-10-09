class Coche:
    def __init__(self, marca, modelo,año):
        self.marca = marca
        self.modelo = modelo 
        self.año = año 
        self._kilometraje = 0 #atrivuto protejido

    def encender(self):
        print(f'el coche {self.marca} {self.modelo} ha sido encendio ')

    def conducir(self, km):
        if km > 0:
            self._kilometraje += km 
            print(f'el coche {self.marca}  ha recorrido {km} km')
        else :
            print('los kilometros deben ser positivos')
    
    def mostrar_kilometraje(self):
        print(f'el coche {self.marca} tiene {self._kilometraje} km recorridos.')
    
mi_coche = Coche('toyota,','corolla', 2024)
mi_coche.encender()
mi_coche.conducir(35)
mi_coche.mostrar_kilometraje()