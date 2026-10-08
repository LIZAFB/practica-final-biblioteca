class Prestamo:

    contador = 0
    def __init__(self, ejemplar, usuario, fecha_prestamo):
        Prestamo.contador += 1
        self.id_prestamo = Prestamo.contador
        self.ejemplar = ejemplar
        self.usuario = usuario
        self.fecha_prestamo = fecha_prestamo
        self.estado = True

    def cambio_estado_ejemplar(self):
        
        if self.ejemplar.estado == True:
            self.ejemplar.estado = False
            return True
        else:
            return False