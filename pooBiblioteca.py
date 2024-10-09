class Biblioteca:
    def __init__(self):
        self.libros = []

    def agregar_libros(self, libro):
        self.libros.append(libro)
        print(f'libro {libro} agregado a la biblioteca')
    
    def eliminar(self,libro):
        if libro in self.libros:
            self.libros.remove(libro)
            print(f'libro {libro} eliminado de la biblioteca')
        else:
            print(f'libro {libro} no encontrado')

    def mostrar_libros(self):
        if self.libros:
            print('libros en la biblioteca', ','.join(self.libros))
        else:
            print('la biblioteca esta vacia ')

biblio = Biblioteca()
biblio.agregar_libros('el caballero de la armadura oxidada')
biblio.mostrar_libros()
biblio.eliminar('el caballero de la armadura oxidada')
biblio.mostrar_libros()