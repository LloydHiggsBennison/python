from funciones import mainMenu, agregarLibro, actualizarLibro, buscarLibro, listarLibros, eliminarLibro
from listaLibros import lista_libros
import os
# agregar Libros, atraves de una funcion (titulo, autor, año de publicacion), utilizando una lista para almacenar diccionarios, cada diccionario es un libro.
# verificar año de publicacion que sea numero positivo, y generar un mensaje de error si no es un numero positivo.

# Actualizar informacion de Libros (recibe el titulo de libro, el nuevo titulo, autor y año de publicacion), 
# si el libro no existe mostrar mensaje de error. manejo de errores posibles.

# Buscar libros por titulo:
# funcion debe recibir el nombre del titulo y devolver informacion completa del libro si es que existe, si no existe mostrar mensaje de error.

# Listar todos los libros
# La función debe imprimir una lista ordenada de todos los libros, mostrando su título, autor y año de publicación.

# Eliminar libros
# La función debe recibir el título del libro y eliminarlo de la biblioteca si existe. Si no existe, debe mostrar un mensaje de error.

# Manejo de errores como entrada de datos no validos, manejo de excepciones con try-except.


while True:
    mainMenu()
    opcion = input("Ingresa el numero de la opcion: ")
    if opcion == "1":
        agregarLibro()
    elif opcion == "2":
        actualizarLibro()
    elif opcion == "3":
        buscarLibro()
    elif opcion == "4":
        listarLibros()
    elif opcion == "5":
        eliminarLibro()
    elif opcion == "6":
        print("Saliendo del programa .... ")
        break
    else:
        print("Ingresa una opcion valida.")
        input("Presiona enter para continuar: ")
        os.system("cls")
