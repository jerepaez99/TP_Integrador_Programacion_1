"""
#• Agregar un país con todos los datos necesarios para almacenarse (No se permiten campos vacios).
#• Actualizar los datos de Población y Superfice de un Pais.
#• Buscar un país por nombre (coincidencia parcial o exacta).
#• Filtrar países por:
# o Continente
# o Rango de población
# o Rango de superficie
#• Ordenar países por:
# o Nombre
# o Población
# o Superficie (ascendente o descendente)
#• Mostrar estadísticas:
# o País con mayor y menor población
# o Promedio de población
# o Promedio de superficie
# o Cantidad de países por continente
"""
import csv
from tp_integrador_1 import ingresar_pais, actualizar_datos, buscar_pais, filtrar_paises, ordenar_paises, existe_pais, estadisticas, obtener_paises, validador, seleccionar_continente, primera_mayuscula
resultado = None
opcion = -1
pais = ""

while opcion != 0:

    print("Menú de opciones:")
    print("1. Agregar país")
    print("2. Actualizar datos de país")
    print("3. Buscar país por nombre")
    print("4. Filtras países")
    print("5. Ordenar países")
    print("6. Mostrar caracteristicas")
    print("0. Salir")

    opcion = (input("Seleccione una opción del 1 al 6, si quiere salir seleccion '0': "))

    if not opcion.isdigit():
        print("No es una opcion valida, por favor ingresa una opcion del 1 al 6, o 0 si queres salir.")
        continue

    opcion = int(opcion)

    if opcion < 0 or opcion > 6:
        print("No es una opcion valida, por favor ingresa una opcion del 1 al 6, o 0 si queres salir.")
        continue

    if opcion == 1:
        nombre = input("Ingrese el nombre del país: ").lower()
        cantidad_habitantes = validador(int(input("ingrese la cantidad de habitantes: ")))
        superficie = validador(int(input("Ingrese la superficie del país expresada en metros cuadrados (expresado unicamente en numeros y sin caracteres especiales: ")))
        continente = seleccionar_continente()
        pais = {"nombre": primera_mayuscula(nombre), "poblacion": cantidad_habitantes, "superficie": superficie, "continente": continente}
        ingresar_pais(pais)

    elif opcion == 2:
        actualizar_datos()

    elif opcion == 3:
       obtener_paises()

    elif opcion == 4:
      filtrar_paises()
            
    elif opcion == 5:
      ordenar_paises()

    elif opcion == 6:
      pass

    elif opcion == 0:
      print("Muchas gracias, los esperamos de vuelta")
      break