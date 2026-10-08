

class Ejemplar:
    def __init__(self,id_ejemplar, libro):
        self.id_ejemplar = id_ejemplar
        self.libro = libro
        self.estado = True
        self.libro.agregar_ejemplar(self)


