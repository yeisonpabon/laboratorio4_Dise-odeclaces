class Termostato:
    def __init__(self, temperatura_inicial):
        self.temperatura = temperatura_inicial
    def aumetar(self,grados):
        self.temperatura += grados
        print(f'la temperatura aumento {grados} °c')
    def disminuir(self,grados):
        self.temperatura -= grados 
        print(f'la temperatura bajo {grados} °c')
    def mostrar_temperatura(self):
        print(f'la temperatura actual es {self.temperatura} °c.')

temp = Termostato(48)
temp.mostrar_temperatura()
temp.aumetar(10)
temp.mostrar_temperatura()
temp.disminuir(40)
temp.mostrar_temperatura()