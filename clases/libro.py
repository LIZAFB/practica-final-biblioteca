#sistema de gestión para una biblioteca

#clase libro
class Libro:
    def __init__(self, titulo, autor, editorial, isbn):
        self.titulo = titulo
        self.autor = autor
        self.editorial = editorial
        self.isbn = isbn
        self.ejemplares = []


    def agregar_ejemplar(self, ejemplar):
        self.ejemplares.append(ejemplar)

        
