from clases import lista_libros
import os

############################################################################################################
# Display de menu principal

def mainMenu():
    print("Menu de la Biblioteca")
    print("1.- Agregar un Libro a Biblioteca")
    print("2.- Actualizar la informacion del Libro")
    print("3.- Buscar un Libro en Biblioteca")
    print("4.- Listar los Libros agregados")
    print("5.- Eliminar un Libro de la Biblioteca")
    print("6.- Salir del programa")


############################################################################################################
# Funcion de agregar libro

def agregarLibro():
    titulo = input("Ingresa el titulo del libro: ").capitalize()
    autor = input("Ingresa el autor del libro: ").capitalize()
    while True:
        try:
            año = int(input("Ingresa el año de publicacion del libro: "))
            if año < 0 :
                print("El año de publicacion debe ser un numero positivo.")
                continue
            elif len(str(año)) != 4:
                print("El año de publicacion debe tener 4 digitos, ejemplo: 2024")
                continue
            break
        except ValueError:
            print("El año de publicacion debe ser un numero positivo.")
    libro = {"Titulo": titulo, 
             "Autor": autor, 
             "Año": año}
    lista_libros.append(libro)
    print(lista_libros)
    input("Presiona enter para continuar: ")
    os.system("cls")



############################################################################################################
# Funcion para editar la informacion del libro

def actualizarLibro():
    index = 1
    for libro in lista_libros:
        print(f"{index}.- Titulo: {libro['Titulo']}")
    titulo = input("Ingresa el titulo del libro a actualizar: ")
    for libro in lista_libros:
        if libro["Titulo"] == titulo:
            nuevo_titulo = input("Ingresa el nuevo titulo: ")
            nuevo_autor = input("Ingresa el nuevo autor: ")
            while True:
                try:
                    nuevo_año = int(input("Ingresa el nuevo año de publicacion: "))
                    if nuevo_año < 0:
                        print("El año de publicacion debe ser un numero positivo.")
                        continue
                    break
                except ValueError:
                    print("El año de publicacion debe ser un numero positivo.")
            libro["Titulo"] = nuevo_titulo
            libro["Autor"] = nuevo_autor
            libro["Año"] = nuevo_año
            print(lista_libros)
            input("Presiona enter para continuar: ")
            os.system("cls")
            return
    print("Libro no encontrado.")
    input("Presiona enter para continuar: ")
    os.system("cls")



############################################################################################################
# Funcion para buscar un libro

def buscarLibro():
    if len(lista_libros) == 0:
        print("No hay libros en la biblioteca.")
        input("Presiona enter para continuar: ")
        os.system("cls")
        return
    titulo = input("Ingresa el titulo del libro a buscar: ").capitalize()
    for libro in lista_libros:
        if libro["Titulo"] == titulo:
            print(f"Titulo: {libro['Titulo']} - Autor: {libro['Autor']} - Año de publicacion: {libro['Año']}")
            input("Presiona enter para continuar: ")
            return
    print("Libro no encontrado.")
    input("Presiona enter para continuar: ")
    os.system("cls")

############################################################################################################

# Funcion para listar todos los libros
def listarLibros():
    index = 1
    for libro in lista_libros:
        print(f"{index}.- Titulo: {libro['Titulo']} - Autor: {libro['Autor']} - Año de publicacion: {libro['Año']}")
        index += 1
    input("Presiona enter para continuar: ")
    os.system("cls")

############################################################################################################
# Funcion para eliminar libros
def eliminarLibro():
    index = 1
    for libro in lista_libros:
        print(f"{index}.- {libro['Titulo']}")
        index += 1
    opcion = int(input("Selecciona el libro a eliminar: "))
    if opcion > 0 and opcion <= len(lista_libros):
        libro_eliminado = lista_libros.pop(opcion - 1)
        print(f"Libro '{libro_eliminado['Titulo']}' eliminado.")
    else:
        print("Opción inválida.")
    input("Presiona enter para continuar: ")
    os.system("cls")
