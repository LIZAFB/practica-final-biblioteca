

from re import I

from clases import usuario
from clases import ejemplar
from clases.biblioteca import Biblioteca
from clases.devolucion import Devolucion
from clases.ejemplar import Ejemplar
from clases.libro import Libro
from clases.prestamo import Prestamo
from clases.usuario import Usuario


def main():
    biblioteca = Biblioteca()

    while True:
        mostrar_menu()
        opcion = input("Escoge una opcion: ")
        if opcion == "1":
            registrar_libro(biblioteca)
        elif opcion == "2":
            registrar_ejemplar(biblioteca)
        elif opcion == "3":
            registrar_usuario(biblioteca)
        elif opcion == "4":
            registrar_prestamo(biblioteca)
        elif opcion == "5":
            registrar_devolucion(biblioteca)
        elif opcion == "6":
            break

    for libro in biblioteca.listado_libros:
        print(libro.titulo) 


def mostrar_menu():
    print("1. Registrar libro")
    print("2. Registrar ejemplar")
    print("3. Registrar usuario")
    print("4. Registrar prestamo")
    print("5. Registrar devolucion")
    print("6. Salir")
def registrar_libro(biblioteca):
    titulo = input("Escribe el título: ")
    autor = input("Escribe el autor: ")
    editorial = input("Escribe la editorial: ")
    isbn = input("Escribe el ISBN: ")
    libro = Libro(titulo, autor, editorial, isbn)
    biblioteca.ingresar_libros(libro)
    print(f"Libro '{titulo}' registrado exitosamente.")
    return libro

def registrar_ejemplar(biblioteca):
    id_ejemplar = input("Escribe el ID del ejemplar: ")
    titulo_libro = input("Escribe el título del libro: ")
    libro = biblioteca.consultar_libro_titulo(titulo_libro)
    if libro is None:
        print(f"No se encontró un libro con el título '{titulo_libro}'.")
        return None
    ejemplar = Ejemplar(id_ejemplar, libro)
    print(f"Ejemplar con ID '{id_ejemplar}' registrado exitosamente.")
    return ejemplar


def registrar_usuario(biblioteca):
    
    nombre = input("Escribe el nombre: ")
    apellido = input("Escribe el apellido: ")
    id = input("Escribe el id: ")
    email = input("Escribe el email: ")
    direccion = input("Escribe la direccion: ")
    telefono = input("Escribe el telefono: ")
    usuario = Usuario(nombre, apellido, id, email, direccion, telefono)
    biblioteca.ingresar_usuarios(usuario)
    print(f"Usuario '{nombre} {apellido}' registrado exitosamente.")
    return usuario

 #registrar    prestamo con ejemplar_id del libro e id del usuario
def registrar_prestamo(biblioteca):
    id_usuario = input("Escribe el ID del usuario: ")
    titulo_libro = input("Escribe el título del libro: ")
    fecha_prestamo = input("Escribe la fecha de préstamo (YYYY-MM-DD): ")

    libro = biblioteca.consultar_libro_titulo(titulo_libro)
    
    
    if libro is None:
        print("No se encontró un libro con el título")
        return None

    ejemplar = biblioteca.consultar_ejemplar(libro)

    if ejemplar is None:
        print(f"No hay ejemplares disponibles para el libro '{libro.titulo}'.")
        return None
    
    usuario = biblioteca.consultar_usuario_id(id_usuario)

    if usuario is None:
        print(f"No se encontró un usuario con el ID '{id_usuario}'.")
        return None
    
    prestamo = Prestamo(ejemplar, usuario, fecha_prestamo)

    if not prestamo.cambio_estado_ejemplar():
        print("El ejemplar no está disponible para préstamo.")
        return None

    biblioteca.ingresar_prestamos(prestamo)
    prestamo.usuario.add_lista_prestamos(prestamo)  # Agrega el préstamo a la lista de préstamos activos del usuario
    print("Préstamo registrado exitosamente ")
    return prestamo


def registrar_devolucion(biblioteca):
   id_usuario = input("Escribe el ID del usuario: ")
   usuario = biblioteca.consultar_usuario_id(id_usuario)

   if usuario is None:
        print(f"No se encontró un usuario con el ID '{id_usuario}'.")
        return None

   prestamos_activos = usuario.prestamos_activos

   if not prestamos_activos:
        print("El usuario no tiene préstamos activos.")
        return None

   titulo_libro = input("Escribe el título del libro a devolver: ")

   prestamo_encontrado = None

   for prestamo in prestamos_activos:
        if prestamo.ejemplar.libro.titulo == titulo_libro:
            prestamo_encontrado = prestamo
            break


   if prestamo_encontrado is None:
        print(f"No se encontró un préstamo activo para el libro '{titulo_libro}'.")
        return None
   
   fecha_devolucion = input("Escribe la fecha de devolución (YYYY-MM-DD): ")
   
   
   devolucion = Devolucion(prestamo_encontrado, fecha_devolucion)
   
   resultado = devolucion.devolucion_exitosa()

   if resultado:
        print("Devolución exitosa ")
   else:
        print("Error en la devolución. El préstamo ya había sido devuelto.")
   return devolucion

  
if __name__ == "__main__":
    main()