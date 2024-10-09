class Temporizador:
    def __init__(self, tiempo_inicial):
        self.tiempo_restante = tiempo_inicial

    def iniciar(self):
        print(f'temporizador iniciado con {self.tiempo_restante} segundos')
    
    def pausar(self):
        print(f'temporizador pausado con {self.tiempo_restante} segundos restantes')
    
    def mostrar(self):
        print(f'tiempo restante: {self.tiempo_restante} segundos')
    

reg = Temporizador(10)
reg.iniciar()
reg.mostrar()
reg.pausar()
reg.mostrar()