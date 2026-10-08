

class Biblioteca :
    def __init__(self):
        self.listado_libros = []
        self.listado_usuarios = []
        self.listado_prestamos = []

    def consultar_libro_titulo(self, titulo):
        
        for libro in self.listado_libros:
            if libro.titulo == titulo:
                return libro
        return None

    def consultar_ejemplar(self,libro):
        for ejemplar in libro.ejemplares:
            if ejemplar.estado == True:
                return ejemplar
        return None
    def consultar_prestamo_id(self, id_prestamo):
        for prestamo in self.listado_prestamos:
            if prestamo.id_prestamo == id_prestamo:
                return prestamo
        return None

    def consultar_usuario_id(self, id_usuario):
        for usuario in self.listado_usuarios:
            if usuario.id == id_usuario:
                return usuario
        return None
    

    def ingresar_usuarios(self, usuario):
        self.listado_usuarios.append(usuario)

    def ingresar_prestamos(self, prestamo):
        self.listado_prestamos.append(prestamo)
        
    def ingresar_libros(self, libro):
        self.listado_libros.append(libro)