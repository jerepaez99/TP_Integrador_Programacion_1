# Desarrollar una aplicación en Python que permita gestionar información sobre países, aplicando listas, diccionarios, 
#funciones, estructuras condicionales y repetitivas, ordenamientos y estadísticas. El sistema debe ser capaz de leer 
#datos desde un archivo CSV, realizar consultas y generar indicadores clave a partir del dataset.
#El objetivo principal es afianzar el uso de estructuras de datos, modularización con funciones y 
#técnicas de filtrado/ordenamiento, aplicando los conceptos aprendidos en Programación 1.

import csv
import os

NOMBRE_ARCHIVO = "datos.csv"

continentes = [
    "América",
    "Asia",
    "Europa",
    "Africa",
    "Oceanía"
]

rangos_poblacionales = [
    "Menos de 1 millón (micro-naciones)",
    "Entre 1 y 10 millones (países pequeños-medianos)",
    "Entre 10 y 100 millones (países medianos-grandes)",
    "Más de 100 millones (gigantes demográficos)"
]

tuplas_poblacionales = [
    (0, 1000000),           # Menos de 1 millón         
    (1000000, 10000000),        # Entre 1 y 10 millones
    (10000000, 100000000),      # Entre 10 y 100 millones
    (100_000_000, float("inf"))       # Más de 100 millones
]


rangos_superficies = [
    "Menos de 10 000 km² (países muy pequeños)",
    "Entre 10 000 y 100 000 km² (países pequeños-medianos)",
    "Entre 100 000 y 1 000 000 km² (países medianos-grandes)",
    "Más de 1 000 000 km² (países muy extensos)"
]

tuplas_superficie = [
    (0, 10000),             # Menos de 10.000 kkm2
    (10000, 100000),       # Entre 10.000 y 100.000 kkm2
    (100000, 1000000),    # Entre 100.000 y 1.000.000 kkm2
    (1000000, float("inf"))        # Más de 1.000.000 kkm2
]

def obtener_paises():
    paises = []
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
    
def guardar_cambios(paises):
  with open(NOMBRE_ARCHIVO, "w", newline="", encoding="utf-8") as archivo:
    escritor = csv.DictWriter(archivo, fieldnames=["nombre", "poblacion", "superficie", "continente"])
    escritor.writeheader()
    escritor.writerows(paises)
    

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
    
def seleccionar_poblacion():
    input_user = ""
    n = 1
    while input_user == "":
        for rango_poblacional in rangos_poblacionales:
            print(f"{n}: {rango_poblacional}")
            n += 1
        input_user = int(input("Seleccione un rango poblacional: "))
        rango = rangos_poblacionales[input_user - 1]
        
        match rango:
            case "Menos de 1 millón (micro-naciones)":
                return tuplas_poblacionales[0]
            case "Entre 1 y 10 millones (países pequeños-medianos)":
                return tuplas_poblacionales[1]
            case "Entre 10 y 100 millones (países medianos-grandes)":
                return tuplas_poblacionales[2]
            case "Más de 100 millones (gigantes demográficos)":
                return tuplas_poblacionales[3]
            
def seleccionar_superficie():
    input_user = ""
    n = 1
    while input_user == "":
        for rango_superficie in rangos_superficies:
            print(f"{n}: {rango_superficie}")
            n += 1
        input_user = int(input("Seleccione un rango de superficie: "))
        rango = rangos_superficies[input_user - 1]
        
        match rango:
            case "Menos de 10 000 km² (países muy pequeños)":
                return tuplas_superficie[0]
            case "Entre 10 000 y 100 000 km² (países pequeños-medianos)":
                return tuplas_superficie[1]
            case "Entre 100 000 y 1 000 000 km² (países medianos-grandes)":
                return tuplas_superficie[2]
            case "Más de 1 000 000 km² (países muy extensos)":
                return tuplas_superficie[3]


def validador(variable):
    while True:
        if variable <= 0:
            variable = int(input("Ingrese un número válido "))
        else:
            return variable

def existe_pais(nombre):
  paises = obtener_paises()
  for pais in paises:
    if pais["nombre"].lower().strip().replace(" ","") == nombre.lower().strip().replace(" ",""):
      return True
  return False


def actualizar_datos():
    nombre = input("Ingrese el nombre del pais para actualizar sus datos: ")
    paises = obtener_paises()
    if existe_pais(nombre):
        input_usuario_actualizar = input("Seleccione 'p' si desea modificar la población o 's' modificar la superficie o 'a' si desea modificar ambas: ").lower().strip()
        match input_usuario_actualizar:
            case "p":
                for pais in paises:
                    if pais["nombre"].lower().strip().replace(" ","") == nombre.lower().strip().replace(" ",""):
                        cantidad_habitantes = validador(int(input("ingrese la nueva cantidad de habitantes: ")))
                        pais["poblacion"] = cantidad_habitantes
                        guardar_cambios(paises)
                print("Accion realizada con éxito")
            case "s":
                for pais in paises:
                    if pais["nombre"].lower().strip().replace(" ","") == nombre.lower().strip().replace(" ",""):
                        superficie = validador(int(input("Ingrese la nueva superficie del país expresada en kilómetros cuadrados: ")))
                        pais["superficie"] = superficie
                        guardar_cambios(paises)
                print("Accion realizada con éxito")
            case "a":
                for pais in paises:
                    if pais["nombre"].lower().strip().replace(" ","") == nombre.lower().strip().replace(" ",""):
                        cantidad_habitantes = validador(int(input("ingrese la nueva cantidad de habitantes: ")))
                        pais["poblacion"] = cantidad_habitantes
                        superficie = validador(int(input("Ingrese la nueva superficie del país expresada en kilómetros cuadrados: ")))
                        pais["superficie"] = superficie
                        guardar_cambios(paises)
                print("Accion realizada con éxito")
            case _:
                print("Opción inváida, intente nuevamente")
    else:    
        print("El pais ingresado no existe: ")
        return

def buscar_pais():
    nombre = input("Ingrese el nombre del pais para obtener sus datos: ")
    paises = obtener_paises()
    if existe_pais(nombre):
        for pais in paises:
            if pais["nombre"].lower().strip().replace(" ","") == nombre.lower().strip().replace(" ",""):
                print(f"País: {pais["nombre"]}, Cantidad de Habitantes: {pais["poblacion"]}, Superficie total: {pais["superficie"]}km2, Continente: {pais["continente"]}")
    else:
        print("El pais ingresado no existe")
        return

def filtrar_paises():
    paises = obtener_paises()
    input_usuario_filtrar = input("Seleccione 'C' si desea filtrar por continente o 'P' si desea filtrar por rango de población o 'S' si desea filtrar por superficie: ").lower().strip()
    match input_usuario_filtrar:
        case "c":
            continente = seleccionar_continente()
            for pais in paises:
                if pais["continente"].lower().strip().replace(" ","") == continente.lower().strip().replace(" ",""):
                    print(f"País: {pais["nombre"]}, Cantidad de Habitantes: {pais["poblacion"]}, Superficie total: {pais["superficie"]}km2, Continente: {pais["continente"]}")
        case "p":
            rango_poblacional = seleccionar_poblacion()
            for pais in paises:
                if pais["poblacion"] >= rango_poblacional[0] and pais["poblacion"] <= rango_poblacional[1]:
                    print(f"País: {pais["nombre"]}, Cantidad de Habitantes: {pais["poblacion"]}, Superficie total: {pais["superficie"]}km2, Continente: {pais["continente"]}")
        case "s":
            rangos_superficie = seleccionar_superficie()
            for pais in paises:
                if pais["superficie"] >= rangos_superficie[0] and pais["superficie"] <= rangos_superficie[1]:
                    print(f"País: {pais["nombre"]}, Cantidad de Habitantes: {pais["poblacion"]}, Superficie total: {pais["superficie"]}km2, Continente: {pais["continente"]}")

def ordenador(criterio, orden):
    paises = obtener_paises()
    cantidad_paises = len(paises)
    if orden == "d":
        for indice_pasada in range(cantidad_paises):
                    for indice_actual in range(cantidad_paises - 1 - indice_pasada):
                        if paises[indice_actual][criterio] > paises[indice_actual + 1][criterio]:
                            paises[indice_actual], paises[indice_actual + 1] = paises[indice_actual + 1], paises[indice_actual]
        return paises.reverse()
    else:
        for indice_pasada in range(cantidad_paises):
                    for indice_actual in range(cantidad_paises - 1 - indice_pasada):
                        if paises[indice_actual][criterio] > paises[indice_actual + 1][criterio]:
                            paises[indice_actual], paises[indice_actual + 1] = paises[indice_actual + 1], paises[indice_actual]
        return paises


def ordenar_paises():
    input_usuario_ordenar = input("Seleccione 'N' si desea ordenar por nombre o 'P' si desea ordenar por población o 'S' si desea ordenar por superficie: ").lower().strip()
    input_usuario_descendente_ascendente = input("Seleccione 'd' si desea que se puestre en orden descendente o 'a' si desea que se muestre en orden ascendente: ").lower().strip()
    match input_usuario_ordenar:
        case "p":
            match input_usuario_descendente_ascendente:
                case "a":
                    paises = ordenador("poblacion","")
                    for pais in paises:
                        print(f"País: {pais["nombre"]}, Cantidad de Habitantes: {pais["poblacion"]}, Superficie total: {pais["superficie"]}km2, Continente: {pais["continente"]}")
                case "d":
                    paises = ordenador("poblacion","d")
                    for pais in paises:
                        print(f"País: {pais["nombre"]}, Cantidad de Habitantes: {pais["poblacion"]}, Superficie total: {pais["superficie"]}km2, Continente: {pais["continente"]}")
                case _:
                    print("Opción inválida, intente nuevamente")
        case "s":
            match input_usuario_descendente_ascendente:
                case "a":
                    paises = ordenador("superficie","")
                    for pais in paises:
                        print(f"País: {pais["nombre"]}, Cantidad de Habitantes: {pais["poblacion"]}, Superficie total: {pais["superficie"]}km2, Continente: {pais["continente"]}")
                case "d":
                    paises = ordenador("superficie","d")
                    for pais in paises:
                        print(f"País: {pais["nombre"]}, Cantidad de Habitantes: {pais["poblacion"]}, Superficie total: {pais["superficie"]}km2, Continente: {pais["continente"]}")
                case _:
                    print("Opción inválida, intente nuevamente")
        case "n":
            match input_usuario_descendente_ascendente:
                case "a":
                    paises = ordenador("nombre","")
                    for pais in paises:
                        print(f"País: {pais["nombre"]}, Cantidad de Habitantes: {pais["poblacion"]}, Superficie total: {pais["superficie"]}km2, Continente: {pais["continente"]}")
                case "d":
                    paises = ordenador("nombre","d")
                    for pais in paises:
                        print(f"País: {pais["nombre"]}, Cantidad de Habitantes: {pais["poblacion"]}, Superficie total: {pais["superficie"]}km2, Continente: {pais["continente"]}")
                case _:
                    print("Opción inválida, intente nuevamente")
        case _:
                    print("Opción inválida, intente nuevamente")

def estadisticas():
    paises = ordenador("poblacion","")
    total_poblacion = 0
    total_superficie = 0

    for pais in paises:
        total_poblacion += int(pais["poblacion"])
        total_superficie += int(pais["superficie"])

    promedio_poblacion = total_poblacion / len(paises)
    promedio_superficie = total_superficie / len(paises)

    opciones_menu_estadisticas =  ["1. Mostrar países con mayor y menor población",
                  "2. Mostrar el promedio de población",
                  "3. Mostrar el promedio por superficie",
                  "4. Mostrar la cantidad de países por continente"]
    for opcion in opciones_menu_estadisticas:
        print(opcion)

    opcion_usuario = input("Seleccione una de las opciones: ")

    match opcion_usuario:
        case "1":
            mayor_poblacion = paises[-1]
            menor_poblacion = paises[0]
            print(f"El país con mayor población es {mayor_poblacion["nombre"]}, con {mayor_poblacion["poblacion"]} habitantes")
            print(f"El país con menor población es {menor_poblacion["nombre"]}, con {menor_poblacion["poblacion"]} habitantes")
        case "2":
            print(f"El promedio de población de todos los países dentro de la base de datos es: {promedio_poblacion}km2")
        case "3":
            print(f"El promedio de superficie de todos los países dentro de la base de datos es: {promedio_superficie}")
        case "4":
            for continente in continentes:
                cantidad_continente = 0
                for pais in paises:
                    if continente == pais["continente"]:
                        cantidad_continente += 1
                print(f"{continente} = {cantidad_continente}")     
    

'''   
nombre = input("Ingrese el nombre del país: ").lower()
cantidad_habitantes = validador(int(input("ingrese la cantidad de habitantes: ")))
superficie = validador(int(input("Ingrese la superficie del país expresada en metros cuadrados: ")))
continente = seleccionar_continente()
pais = {"nombre": primera_mayuscula(nombre), "poblacion": cantidad_habitantes, "superficie": superficie, "continente": continente}
ingresar_pais(pais)

'''