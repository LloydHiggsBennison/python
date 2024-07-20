from funciones import mainMenu, agregarLibro, actualizarLibro, buscarLibro, listarLibros, eliminarLibro, buscarSKU, cargarUsuarios, verLibrosDisponibles
from listaLibros import lista_libros
import os

# Se incorpora la función cargarUsuarios para cargar la lista de usuarios

usuarios = cargarUsuarios()
if not usuarios:
    print("No se pudo cargar la lista de usuarios. Verifica el archivo de usuarios.")
    exit()

print("Bienvenido a la biblioteca virtual.")
print("")
print("Introduce tu usuario y contraseña")
print("")

# Se modifica el login para que el usuario pueda intentar ingresar hasta 3 veces
# Se valida si el usuario es administrador o usuario normal
# Se genera un inicio de sesion con contraseña para acceder a biblioteca.


intentos = 0
usuario_valido = False

while intentos < 3:
    usuario_input = input("Usuario: ")
    contrasena_input = input("Contraseña: ")
    for usuario in usuarios:
        if usuario["usuario"] == usuario_input and usuario["contrasena"] == contrasena_input:
            usuario_valido = True
            if usuario_input == "admin":
                print("Bienvenido administrador.")
                input("Presiona enter para continuar: ")
                os.system("cls")
            else:
                print("Bienvenido usuario.")
                input("Presiona enter para continuar: ")
                os.system("cls")
            break
    if usuario_valido:
        break
    else:
        print("Usuario o contraseña incorrectos. Intenta de nuevo.")
        intentos += 1

if not usuario_valido:
    print("Has excedido el número máximo de intentos. Saliendo del programa...")
    exit()

#  Se modifica el menu, en caso de no haber libros en la lista, se muestra un mensaje y se sale del programa

while True:
    mainMenu(lista_libros)
    print("")
    opcion = input("Ingresa el numero de la opcion: ")
    if opcion == "1":
        agregarLibro(lista_libros)
    elif opcion == "2":
        if not lista_libros:
            print("Saliendo del programa .... ")
            input("Presiona enter para continuar: ")
            os.system("cls")
            break
        else:
            actualizarLibro(lista_libros)
    elif opcion == "3":
        buscarLibro(lista_libros)
    elif opcion == "4":
        verLibrosDisponibles(lista_libros)
    elif opcion == "5":
        listarLibros(lista_libros)
    elif opcion == "6":
        eliminarLibro(lista_libros)
    elif opcion == "7":
        buscarSKU(lista_libros)
    elif opcion == "8":
        print("Saliendo del programa .... ")
        break
    else:
        print("Ingresa una opcion valida.")
        input("Presiona enter para continuar: ")
        os.system("cls")
