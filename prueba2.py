from funciones import mainMenu, agregarLibro, actualizarLibro, buscarLibro, listarLibros, eliminarLibro
from listaLibros import lista_libros
import os

################################################################
# Menu principal

while True:
    mainMenu()
    print("")
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

################################################################
