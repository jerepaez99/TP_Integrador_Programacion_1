import csv
from tp_integrador_1 import ingresar_pais, actualizar_datos, buscar_pais, filtrar_paises, ordenar_paises, existe_pais, estadisticas, obtener_paises, validador, seleccionar_continente, primera_mayuscula
opcion = -1
pais = ""
intento = 1
eleccion = ""

print("Bienvenido al sistema de gestión de países.")

while opcion != 0:
      
    if intento >3:
        print("Has superado el numero de intentos, el programa se cerrara.")
        break

    print("Menú de opciones:")
    print("1. Agregar país")
    print("2. Actualizar datos de país")
    print("3. Buscar país por nombre")
    print("4. Filtras países")
    print("5. Ordenar países")
    print("6. Mostrar estadisticas")
    print("0. Salir")

    opcion = (input("Seleccione una opción del 1 al 6, si quiere salir seleccion '0': "))

    if not opcion.isdigit(): #Verificamos que el input del usuario sea un numero
        print("No es una opcion valida, por favor ingresa una opcion del 1 al 6, o 0 si queres salir.")
        intento = intento + 1
        continue

    opcion = int(opcion)

    if opcion < 0 or opcion > 6: #Verificamos que este dentro del rango de opciones
        print("No es una opcion valida, por favor ingresa una opcion del 1 al 6, o 0 si queres salir.")
        intento = intento + 1
        continue
    
  

    if opcion == 1:
        nombre = input("Ingrese el nombre del país: ").lower()
        if existe_pais(nombre): #Verificamos que el pais no exista ya en la base de datos
          eleccion = str(input("Ese país ya existe en la base de datos, le gustaría actualizar sus datos?[S/N]: ")).lower()
          if eleccion == "s":
              actualizar_datos()
          elif eleccion == "n":
              print("Volviendo al menú principal.")
              continue

        elif not existe_pais(nombre): #Si no existe en la base de datos, procedemos a pedir los demas datos
          cantidad_habitantes = validador(int(input("ingrese la cantidad de habitantes (Expresado en numeros y sin ',' o '.'): ")))
          superficie = validador(int(input("Ingrese la superficie del país expresada en metros cuadrados (expresado unicamente en numeros y sin caracteres especiales): ")))
          continente = seleccionar_continente()
          pais = {"nombre": primera_mayuscula(nombre), "poblacion": cantidad_habitantes, "superficie": superficie, "continente": continente}
          ingresar_pais(pais)

          input("Presione una tecla para continuar ")

    elif opcion == 2:
        actualizar_datos()
        input("Presione una tecla para continuar ")

    elif opcion == 3:
      buscar_pais()
      input("Presione una tecla para continuar ")
    
    elif opcion == 4:
      filtrar_paises()
      input("Presione una tecla para continuar ")

    elif opcion == 5:
      ordenar_paises()
      input("Presione una tecla para continuar ")

    elif opcion == 6:
      estadisticas()
      input("Presione una tecla para continuar ")
      
    elif opcion == 0:
      print("Muchas gracias, los esperamos de vuelta")
      break