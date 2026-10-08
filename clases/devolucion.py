class Devolucion:
    def __init__(self, prestamo, fecha_devolucion):
        self.prestamo = prestamo
        self.fecha_devolucion = fecha_devolucion

    def devolucion_exitosa(self):
        # Lógica para procesar la devolución del libro
        if self.prestamo.estado:
            self.prestamo.estado = False  # Cambia el estado del préstamo a devuelto
            self.cambio_estado_ejemplar()
            self.prestamo.usuario.eliminar_lista_prestamos(self.prestamo)  # Elimina el préstamo de la lista de préstamos activos del usuario
            return True
        else:
            print("El libro ya ha sido devuelto anteriormente.")
            return False

    def cambio_estado_ejemplar(self):
        if self.prestamo.ejemplar.estado == False:
            self.prestamo.ejemplar.estado = True  # Cambia el estado del ejemplar a disponible
        else:
            return False