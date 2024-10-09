class Album:
    def __init__(self):
        self.fotos = []
    
    def agregar(self,foto):
        self.fotos.append(foto)
        print(f'fotos {foto} agegada al album')

    def eliminar(self,foto):
        if foto in self.fotos:
            self.fotos.remove(foto)
            print(f'foto {foto} eliminada del album')
        else:
            print(f'la foto {foto} no encontrada')

    def mostrar(self):
        if self.fotos:
            print('fotos en  el album')
        else:
            print('el album esta vacio')
            
