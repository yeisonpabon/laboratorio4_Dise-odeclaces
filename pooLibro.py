class Libro:
    def __init__(self, titulo, autor):
        self.titulo= titulo
        self.autor = autor
        self.disponible = True

    def prestar(self):
        if self.disponible:
            self.disponible = False 
            print(f'el libro {self.titulo} del autor {self.autor} ha sido prestado')
        else:
            print(f'el libro {self.titulo} del autor {self.autor} no esta disponible')
    
    def devolver(self):
        self.disponible = True 
        print(f'el libro {self.titulo} del autor {self.autor} ha sido devuelto')

    def mostrar_estado(self):
        estado = 'disponible' if self.disponible else 'prestado'
        print(f'el libro {self.titulo} del  autor {self.autor} está {estado}.')

bestceller = Libro('descarados','Diego')
bestceller.prestar()
bestceller.mostrar_estado()
bestceller.devolver()
bestceller.mostrar_estado()