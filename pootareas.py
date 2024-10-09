class Listadode_tareas:
    def __init__(self):
        self.tareas = []

    def agregar_tareas(self,tarea):
        self.tareas.append(tarea)
        print(f'la tara {tarea} agregada a la lista ')

    def eliminar(self,tarea):
        if tarea in self.tareas:
            self.tareas.remove(tarea)
            print(f'tarea {tarea} eliminada de la lista')
        else:
            print(f'tarea {tarea} no encontrada')
    
    def mostrar_tarea(self):
        if self.tareas:
            print('tareas pendientes:,',''.join(self.tareas))
        else:
            print('no hay tareas pendientes')


hacer = Listadode_tareas()
hacer.agregar_tareas('botar la basura')
hacer.mostrar_tarea()
hacer.eliminar('botar la basura')
hacer.mostrar_tarea()