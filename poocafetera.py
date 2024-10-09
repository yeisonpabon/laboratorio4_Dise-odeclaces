class Cafetera:
    def __init__(self, capacidad):
        self.capacidad = capacidad 
        self.nivel_actual : 0

    def llenar(self):
        self.nivel_actual = self.capacidad
        print('la cafetera ha sido llenada')
    
    def servir_taza(self):
        if self.nivel_actual > 0:
            self.nivel_actual -= 1
            print('se ha servido una taza de cafe')
        else :
            print('no hay cafe. Llena la cafetera ')

    def mostrar_nivel(self):
        print(f'nivel actual de cafe: {self.nivel_actual} tazas.')

cafe = Cafetera(2)
cafe.llenar()
cafe.mostrar_nivel()
cafe.servir_taza()
cafe.mostrar_nivel()

        
        
