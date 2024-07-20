import json 
from listaLibros import lista_libros
import os
import hashlib

############################################################################################################
# Display de menu principal

def mainMenu(lista_libros):
    print("\n\033[36m### Bienvenidos a la Biblioteca ###\033[0m\n")
    if not lista_libros:
        print("Por favor, agrega un libro para continuar:")
        print("1.- Agregar un Libro a Biblioteca")
        print("2.- Salir del programa")
    else:
        print("Por favor, selecciona una opción:")
        print("1.- Agregar un Libro a Biblioteca")
        print("2.- Actualizar la información del Libro")
        print("3.- Buscar un Libro en Biblioteca")
        print("4.- Buscar los Libros Disponibles")
        print("5.- Listar los Libros agregados")
        print("6.- Eliminar un Libro de la Biblioteca")
        print("7.- Buscar un libro por SKU")
        print("8.- Salir del programa")


############################################################################################################
# Se genera funcion para cargar usuarios
# Y hacer comprobaciones de errores si los usuarios existen o no, tambien para ingresar al sistema

def cargarUsuarios():
    ruta_archivo = os.path.join('E:\\Visual Studio Code\\Python\\Prueba2\\usuarios.json')
    try:
        with open(ruta_archivo, 'r') as archivo:
            datos = json.load(archivo)
            return datos['usuarios']
    except FileNotFoundError:
        print(f"El archivo de usuarios no fue encontrado en la ruta: {ruta_archivo}.")
        return []
    except json.JSONDecodeError:
        print("Error al decodificar el archivo JSON.")
        return []

usuarios = cargarUsuarios()
print(usuarios)

############################################################################################################
# Funcion para agregar libro
# Se agrega validaciones de titulo, autor, año y disponibilidad
# Se agrega un SKU al libro
# Se verifica que los datos no sean largos para que puedan ser guardados en el archivo JSON
# Se agrega strip para eliminar espacios en blanco

def agregarLibro(lista_libros):
    while True:
        titulo = input("Ingresa el titulo del libro: ").capitalize().strip()
        if titulo:
            if len(titulo) > 100:
                print("El título es demasiado largo. Intenta con un título más corto.")
                continue
            break
        else:
            print("El titulo del libro no puede estar vacio.")
    
    while True:
        autor = input("Ingresa el autor del libro: ").capitalize().strip()
        if autor:
            if len(autor) > 100:
                print("El nombre del autor es demasiado largo. Intenta con un nombre más corto.")
                continue
            break
        else:
            print("El autor del libro no puede estar vacio.")
    
    while True:
        try:
            año = input("Ingresa el año de publicacion del libro: ").strip()
            if not año.isdigit() or len(año) != 4 or int(año) < 0:
                print("El año de publicacion debe ser un número positivo de 4 dígitos.")
                continue
            año = int(año)
            break
        except ValueError:
            print("El año de publicacion debe ser un número.")

    while True:
        disponible = input("El libro esta disponible? (si/no): ").strip().lower()
        if disponible == "si":
            disponible = True
            break
        elif disponible == "no":
            disponible = False
            break
        else:
            print("Ingresa 'si' o 'no'.")

    ind_sku = 1
    for libro in lista_libros:
        if libro["SKU"] == f"SKU{ind_sku}":
            ind_sku += 1
    sku = hashlib.sha256(str(ind_sku).encode()).hexdigest()
            
    libro = {"Titulo": titulo, "Autor": autor, "Año": año, "Estado": disponible, "SKU": sku}
    lista_libros.append(libro)
    print(f"El libro '{titulo}' se ha agregado a la biblioteca exitosamente.")
    print(libro)
    input("Presiona enter para continuar: ")
    os.system("cls")


############################################################################################################
# Función para editar la información del libro
# Se agrega strip para eliminar espacios en blanco

def actualizarLibro(lista_libros):
    if not lista_libros:
        print("No hay libros en la biblioteca.")
        input("Presiona enter para continuar: ")
        os.system("cls")
        return

    index = 1
    for libro in lista_libros:
        print(f"{index}.- Titulo: {libro['Titulo']}")
        index += 1

    titulo = input("Ingresa el titulo del libro a actualizar: ").capitalize().strip()
    libro_encontrado = False

    for libro in lista_libros:
        if libro["Titulo"] == titulo:
            libro_encontrado = True
            nuevo_titulo = input("Ingresa el nuevo titulo: ").capitalize().strip()
            nuevo_autor = input("Ingresa el nuevo autor: ").capitalize().strip()

            while True:
                nuevo_año = input("Ingresa el nuevo año de publicacion: ").strip()
                if not nuevo_año.isdigit() or len(nuevo_año) != 4 or int(nuevo_año) < 0:
                    print("El año de publicacion debe ser un número positivo de 4 dígitos.")
                    continue
                nuevo_año = int(nuevo_año)
                break
            cambio_disponible = input("El libro esta disponible? (si/no): ").strip().lower()

            libro["Titulo"] = nuevo_titulo
            libro["Autor"] = nuevo_autor
            libro["Año"] = nuevo_año
            libro["Estado"] = True if cambio_disponible == "si" else False
            print(f"Se ha actualizado la informacion del libro '{titulo}' correctamente.")
            print(libro)
            input("Presiona enter para continuar: ")
            os.system("cls")
            return

    if not libro_encontrado:
        print("Libro no encontrado.")
        input("Presiona enter para continuar: ")
        os.system("cls")


############################################################################################################
# Función para buscar un libro
# Se agrega strip para eliminar espacios en blanco

def buscarLibro(lista_libros):
    if not lista_libros:
        print("No hay libros en la biblioteca.")
        input("Presiona enter para continuar: ")
        os.system("cls")
        return

    titulo = input("Ingresa el titulo del libro a buscar: ").capitalize().strip()

    libro_encontrado = False
    for libro in lista_libros:
        if libro["Titulo"] == titulo:
            print(f"Titulo: {libro['Titulo']} - Autor: {libro['Autor']} - Año de publicacion: {libro['Año']}")
            libro_encontrado = True
            break

    if not libro_encontrado:
        print("Libro no encontrado.")
    else:
        print("Libro encontrado.")

    input("Presiona enter para continuar: ")
    os.system("cls")


############################################################################################################
# Se agrega función para listar los libros disponibles
# Se verifica que el mensaje de los libros no disponibles simplemetne no se muestre

def verLibrosDisponibles(lista_libros):
    if not lista_libros:
        print("No hay libros en la biblioteca.")
        input("Presiona enter para continuar: ")
        os.system("cls")
        return

    for libro in lista_libros:
        if libro["Estado"] == True:
            print(f"Titulo: {libro['Titulo']} - Autor: {libro['Autor']} - Año de publicacion: {libro['Año']}")
    input("Presiona enter para continuar: ")
    os.system("cls")

############################################################################################################
# Función para listar todos los libros
# Se modifica el codigo quitando ciclo while y try para manejo de errores,.
# Se modica el codigo con el index y se agrega enumerate para indice.

def listarLibros(lista_libros):
    if not lista_libros:
        print("No hay libros en la biblioteca.")
        input("Presiona enter para continuar: ")
        os.system("cls")
        return

    for index, libro in enumerate(lista_libros, start=1):
        print(f"{index}.- Titulo: {libro['Titulo']} - Autor: {libro['Autor']} - Año de publicacion: {libro['Año']}")

    input("Presiona enter para continuar: ")
    os.system("cls")


############################################################################################################
# Se agrega función para buscar un libro por SKU
# Se agrega strip a la entrada de SKU para evitar errores de espacios

def buscarSKU(lista_libros):
    if not lista_libros:
        print("No hay libros en la biblioteca.")
        input("Presiona enter para continuar: ")
        os.system("cls")
        return

    sku = input("Ingresa el SKU del libro a buscar: ").strip()

    libro_encontrado = False
    for libro in lista_libros:
        if libro["SKU"] == sku:
            print(f"Titulo: {libro['Titulo']} - Autor: {libro['Autor']} - Año de publicacion: {libro['Año']}")
            libro_encontrado = True
            break

    if not libro_encontrado:
        print("Libro no encontrado.")
    else:
        print("Libro encontrado.")

    input("Presiona enter para continuar: ")
    os.system("cls")


############################################################################################################
# Función para eliminar libros

def eliminarLibro(lista_libros):
    if not lista_libros:
        print("No hay libros en la biblioteca.")
        input("Presiona enter para continuar: ")
        os.system("cls")
        return

    for index, libro in enumerate(lista_libros, start=1):
        print(f"{index}.- {libro['Titulo']}")

    entrada = input("Selecciona el libro a eliminar: ").strip()
    if not entrada.isdigit() or not 0 < int(entrada) <= len(lista_libros):
        print("Opción inválida.")
        input("Presiona enter para continuar: ")
        os.system("cls")
        return

    opcion = int(entrada)
    libro_eliminado = lista_libros.pop(opcion - 1)
    print(f"Libro '{libro_eliminado['Titulo']}' eliminado.")

    input("Presiona enter para continuar: ")
    os.system("cls")
