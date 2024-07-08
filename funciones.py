from listaLibros import lista_libros
import os

############################################################################################################
# Display de menu principal

def mainMenu():
    if len(lista_libros) == 0:    
        print("")
        print("\033[36m### Bienvenidos a la Biblioteca, por favor agrega un libro para continuar: ###\033[0m")
        print("")
        print("1.- Agregar un Libro a Biblioteca")
    else:        
        print("")
        print("\033[36m### Bienvenidos a la Biblioteca, por favor selecciona una opcion ###\033[0m")
        print("")
        print("1.- Agregar un Libro a Biblioteca")
        print("2.- Actualizar la informacion del Libro")
        print("3.- Buscar un Libro en Biblioteca")
        print("4.- Listar los Libros agregados")
        print("5.- Eliminar un Libro de la Biblioteca")
        print("6.- Salir del programa")


############################################################################################################
# Funcion para agregar libro

def agregarLibro():
    while True:
        titulo = input("Ingresa el titulo del libro: ").capitalize()
        if titulo != "":
            break
        print("El titulo del libro no puede estar vacio.")
    while True:
        autor = input("Ingresa el autor del libro: ").capitalize()
        if autor != "":
            break
        print("El autor del libro no puede estar vacio.")
    while True:
        try:
            año = int(input("Ingresa el año de publicacion del libro: "))
            if año < 0 :
                print("El año de publicacion debe ser un numero positivo.")
                continue
            elif len(str(año)) > 4:
                print("El año de publicacion debe tener 4 digitos, ejemplo: 2024")
                continue
            break
        except ValueError:
            print("El año de publicacion debe ser un numero positivo.")
            
    libro = {"Titulo": titulo, 
             "Autor": autor, 
             "Año": año}
    lista_libros.append(libro)
    print(f"El libro '{titulo}' se ha agregado a la biblioteca exitosamente.")
    print(libro)
    input("Presiona enter para continuar: ")
    os.system("cls")



############################################################################################################
# Funcion para editar la informacion del libro

def actualizarLibro():
    while True:
        try:
            if len(lista_libros) == 0:
                print("No hay libros en la biblioteca.")
                input("Presiona enter para continuar: ")
                os.system("cls")
                return
            break
        except ValueError:
            print("No hay libros en la biblioteca.")
    index = 1
    for libro in lista_libros:
        print(f"{index}.- Titulo: {libro['Titulo']}")
        index += 1
    titulo = input("Ingresa el titulo del libro a actualizar: ").capitalize()
    for libro in lista_libros:
        if libro["Titulo"] == titulo:
            nuevo_titulo = input("Ingresa el nuevo titulo: ").capitalize()
            nuevo_autor = input("Ingresa el nuevo autor: ").capitalize()
            while True:
                try:
                    nuevo_año = int(input("Ingresa el nuevo año de publicacion: "))
                    if nuevo_año < 0 :
                        print("El año de publicacion debe ser un numero positivo.")
                        continue
                    elif len(str(nuevo_año)) > 4:
                        print("El año de publicacion debe tener 4 digitos, ejemplo: 2024")
                        continue
                    break
                except ValueError:
                    print("El año de publicacion debe ser un numero positivo.")
            libro["Titulo"] = nuevo_titulo
            libro["Autor"] = nuevo_autor
            libro["Año"] = nuevo_año
            print(f"Se ha actualizado la informacion del libro '{titulo}' correctamente.")
            print(libro)
            input("Presiona enter para continuar: ")
            os.system("cls")
            return
    print("Libro no encontrado.")
    input("Presiona enter para continuar: ")
    os.system("cls")



############################################################################################################
# Funcion para buscar un libro

def buscarLibro():
    while True:
        try:
            if len(lista_libros) == 0:
                print("No hay libros en la biblioteca.")
                input("Presiona enter para continuar: ")
                os.system("cls")
                return
            titulo = input("Ingresa el titulo del libro a buscar: ").capitalize()
            libro_encontrado = False
            for libro in lista_libros:
                if libro["Titulo"] == titulo:
                    print(f"Titulo: {libro['Titulo']} - Autor: {libro['Autor']} - Año de publicacion: {libro['Año']}")
                    libro_encontrado = True
                    break
            if not libro_encontrado:
                print("Libro no encontrado.")
                input("Presiona enter para continuar: ")
                os.system("cls")
                return
            else:
                input("Presiona enter para continuar: ")
                os.system("cls")
                return
        except ValueError:
            print("Se produjo un error")
            input("Presiona enter para continuar: ")
            os.system("cls")

############################################################################################################
# Funcion para listar todos los libros

def listarLibros():
    while True:
        try:
            if len(lista_libros) == 0:
                print("No hay libros en la biblioteca.")
                input("Presiona enter para continuar: ")
                os.system("cls")
                return
            break
        except ValueError:
            print("No hay libros en la biblioteca.")
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
    entrada = input("Selecciona el libro a eliminar: ")
    try:
        opcion = int(entrada) if entrada.strip() != "" else 0
    except ValueError:
        print("Opcion invalida.")
        input("Presiona enter para continuar: ")
        os.system("cls")
        return

    if 0 < opcion <= len(lista_libros):
        libro_eliminado = lista_libros.pop(opcion - 1)
        print(f"Libro '{libro_eliminado['Titulo']}' eliminado.")
    else:
        print("Opcion invalida.")
    
    input("Presiona enter para continuar: ")
    os.system("cls")
