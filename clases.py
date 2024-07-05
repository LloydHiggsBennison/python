# agregar un constructor a la clase Libro que reciba el titulo, autor y año de publicacion.

class agregar_Libro:
    def __init__(self, titulo, autor, año):
        self.titulo = titulo
        self.autor = autor
        self.año = año

    def __str__(self):
        return f"Titulo: {self.titulo} - Autor: {self.autor} - Año de publicacion: {self.año}"
    
lista_libros = []
