class Usuario:
    def __init__(self, nombre, apellido, id, email, direccion, telefono):
        self.nombre = nombre
        self.apellido = apellido
        self.id = id
        self.email = email
        self.direccion = direccion
        self.telefono = telefono
        self.prestamos_activos = []  # Lista para almacenar los préstamos del usuario
        self.historial_prestamos = []

    def add_lista_prestamos(self, prestamo):
        self.prestamos_activos.append(prestamo)       
        self.historial_prestamos.append(prestamo)
        
    def eliminar_lista_prestamos(self, prestamo):
        if prestamo in self.prestamos_activos:
            self.prestamos_activos.remove(prestamo)
        else:
            print("El préstamo no se encuentra en la lista de préstamos activos del usuario.")
        