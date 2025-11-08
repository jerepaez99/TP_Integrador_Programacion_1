# Desarrollar una aplicación en Python que permita gestionar información sobre países, aplicando listas, diccionarios, 
#funciones, estructuras condicionales y repetitivas, ordenamientos y estadísticas. El sistema debe ser capaz de leer 
#datos desde un archivo CSV, realizar consultas y generar indicadores clave a partir del dataset.
#El objetivo principal es afianzar el uso de estructuras de datos, modularización con funciones y 
#técnicas de filtrado/ordenamiento, aplicando los conceptos aprendidos en Programación 1.

import csv
import os

NOMBRE_ARCHIVO = "datos.csv"

continentes = [
    "America",
    "Asia",
    "Europa",
    "Africa",
    "Oceania"
]

#El siguiente bloque de código consulta al archivo "catalogo.csv" y devuelve la lista de libros en forma de diccionarios "TITULO" - "CANTIDAD"
def obtener_paises():
    paises = []
    #Si el archivo no existe, lo crea
    if not os.path.exists(NOMBRE_ARCHIVO):
        with open(NOMBRE_ARCHIVO, "w", newline="", encoding="utf-8") as archivo:
            escritor = csv.DictWriter(archivo, fieldnames=["nombre", "poblacion", "superficie", "continente"])
            escritor.writeheader()
            return paises

    with open (NOMBRE_ARCHIVO, newline="", encoding="utf-8") as archivo:
        lector = csv.DictReader(archivo)
        for fila in lector:
            paises.append({"nombre": fila["nombre"], "poblacion": int(fila["poblacion"]), "superficie": int(fila["superficie"]), "continente": fila["continente"]})
        return paises
    


#El siguiente bloque de código recibe un diccionario "TITULO" - "CANTIDAD" y agrega una nuva línea al final con los valores ingresados por el usuario
def primera_mayuscula(str):
    return str[0].upper() + str[1:]

def ingresar_pais(pais):
    with open(NOMBRE_ARCHIVO, "a", newline="", encoding="utf-8") as archivo:
        escritor = csv.DictWriter(archivo, fieldnames=["nombre", "poblacion", "superficie", "continente"])
        escritor.writerow(pais)

def seleccionar_continente():
    input_user = ""
    n = 1
    while input_user == "":
        for continente in continentes:
            print(f"{n}: {continente}")
            n += 1
        input_user = int(input("Seleccione un continente: "))
        return continentes[input_user - 1]




nombre = input("Ingrese el nombre del país: ").lower()
cantidad_habitantes = int(input("ingrese la cantidad de habitantes: "))
superficie = int(input("Ingrese la superficie del país expresada en metros cuadrados: "))
continente = seleccionar_continente()
pais = {"nombre": primera_mayuscula(nombre), "poblacion": cantidad_habitantes, "superficie": superficie, "continente": continente}
ingresar_pais(pais)


'''   

#El siguiente bloque de código recibe una cadena y checkea si esa cadena se encuentra dentro de los "TITULO" del csv. Devuelve un booleano, 
#si existe devuelve "True" si no "False"
def existe_libro(nombre):
  libros = obtener_libros()
  for libro in libros:
    if libro["TITULO"].lower().strip().replace(" ","") == nombre.lower().strip().replace(" ",""):
      return True
  return False


def ingresar_ejemplares():
    nombre = input("Ingrese el nombre del título para agregar los ejemplares: ")
    #Checkea si existe el libro
    if existe_libro(nombre):
        #Obtiene la lista de diccionarios
        libros = obtener_libros()
        #Busca en cada diccionario hasta dar con el título que coloca el usuario
        for libro in libros:
            if libro["TITULO"].lower().strip().replace(" ","") == nombre.lower().strip().replace(" ",""):
                cantidad = int(input("Ingrese la cantidad de ejemplares que desea añadir: "))
                #Añade la cantidad correspondiente ingresada por el usuario
                libro["CANTIDAD"] += cantidad
                #Guarda los cambios del CSV
                guardar_cambios(libros)

        print("Accion realizada con éxito")

    else:    
        print("El libro ingresado no existe: ")
        return


def mostrar_catalogo():
    #Recibe la lista de diccionarios
    libros = obtener_libros()
    #La recorre e imprime cada uno de los valores de forma ordenada
    for libro in libros:
        print(f"Titulo: {libro["TITULO"]}, Cantidad de ejemplares disponibles: {libro["CANTIDAD"]}")

#Recibe una cadena
def consultar_disponibilidad(nombre):
    #Recibe la lista de diccionarios
    libros = obtener_libros()
    #Checkea si la cadena condice con un título disponible
    if existe_libro(nombre):
        #Recorre el diccionario
        for libro in libros:
            if libro["TITULO"].lower().strip().replace(" ","") == nombre.lower().strip().replace(" ",""):
                #Devuelve de forma ordenada la cantidad de ejemplares utilizando los valores del diccionario
                print(f"La cantidad de ejemplares disponibles de {libro["TITULO"]} es: {libro["CANTIDAD"]}")
    else:
        print("El libro ingresado no se encuentra en la base de datos")


def listar_agotados():
    #Recibe la lista de diccionarios
    libros = obtener_libros()
    #La recorre
    for libro in libros:
        #Si uno de ellos, en el valor "CANTIDAD" presenta un 0, devuelve el valor "TÍTULO"
        if libro["CANTIDAD"] == 0:
            print(f"{libro["TITULO"]}")


def actualizar_ejemplares(nombre):
    #Recibe la lista de diccionarios
    libros = obtener_libros()
    #Checkea si la cadena condice con un título disponible
    if existe_libro(nombre):
        #Recibe el input del usuario, d para devolucion p para préstamo
        input_usuario_actualizar = input("Seleccione 'd' si desea cargar una devolución o 'p' si desea cargar un préstamo: ").lower().strip()
        
        match input_usuario_actualizar:
            case "d":
                #Recorre el diccionario
                for libro in libros:
                    if libro["TITULO"].lower().strip().replace(" ","") == nombre.lower().strip().replace(" ",""):
                        #Suma 1 a la cantidad existente y guarda los cambios
                        libro["CANTIDAD"] += 1
                        guardar_cambios(libros)
                        print("Accion realizada con éxito")
            case "p":
                #Recorre el diccionario
                for libro in libros:
                    if libro["TITULO"].lower().strip().replace(" ","") == nombre.lower().strip().replace(" ",""):
                        #Checkea que hayan existencias del libro para poder dar el préstamo
                        if libro["CANTIDAD"] >= 1:
                            #Resta 1 a la cantidad existente
                            libro["CANTIDAD"] -= 1
                            guardar_cambios(libros)
                            print("Accion realizada con éxito")
                        #En caso de que las existencias no sean suficientes avisa al usuario
                        else:
                            print("No contamos con suficientes existencias")
            case _:
                print("Opcion no válida")          
    else:
        print("El libro ingresado no se encuentra en la base de datos")

#sobreescribe el archivo CSV con la información actualizada de los libros, asegurando que cada registro se guarde correctamente con sus columnas "TITULO" y "CANTIDAD".
def guardar_cambios(libros):
  with open(NOMBRE_ARCHIVO, "w", newline="", encoding="utf-8") as archivo:
    escritor = csv.DictWriter(archivo, fieldnames=["TITULO", "CANTIDAD"])
    escritor.writeheader()
    escritor.writerows(libros)


opciones_menu =  ["1. Ingresar títulos (multiples)",
                  "2. Ingresar ejemplares para un título existente",
                  "3. Mostrar Catálogo",
                  "4. Consultar disponibilidad de un título en particular",
                  "5. Listar agotados",
                  "6. Agregar título a la base de datos con un ejemplar",
                  "7. Actualizar ejemplares (préstamo/devolución)",
                  "8. Salir"]


#Cada uno de las opciones llama a la funcion correspondiente, de ser necesario se le pide al usuario informacion para completar los parámetros necesarios
while True:
    for opcion in opciones_menu:
        print(opcion)
    
    obtener_libros()
    
    input_usuario = input("Seleccione una opción: ").strip()

    match input_usuario:
        case "1":
            repetir = "y"

            while repetir == "y":
                nombre = input("Ingrese el titulo del libro: ").lower()
                cantidad = int(input("ingrese la cantidad de libros: "))
                titulo = {"TITULO": nombre, "CANTIDAD": cantidad}
                ingresar_titulo(titulo)
                repetir = input("Si desea agregar otro título ingrese 'y', presione cualquier otra tecla para continuar: ").lower().strip()

        case "2":
            ingresar_ejemplares()
            input("Presione una tecla para continuar ")
        
        case "3":
            mostrar_catalogo()
            input("Presione una tecla para continuar ")

        case "4":
            nombre = input("Ingrese el nombre del libro del que desea consultar disponibilidad: ")
            consultar_disponibilidad(nombre)
            input("Presione una tecla para continuar ")

        case "5":
            listar_agotados()
            input("Presione una tecla para continuar ")

        case "6":
            nombre = input("Ingrese el titulo del libro: ").lower()
            cantidad = 1
            titulo = {"TITULO": nombre, "CANTIDAD": cantidad}
            ingresar_titulo(titulo)
            input("Presione una tecla para continuar ")

        case "7":
            nombre = input("Ingrese el titulo del libro: ").lower()
            actualizar_ejemplares(nombre)
            input("Presione una tecla para continuar ")

        case "8":
            break

        case _:
            print("Opción no válida")

            '''