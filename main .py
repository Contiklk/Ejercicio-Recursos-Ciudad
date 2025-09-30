import resource_management as rm
import edificios as ed
import time

paso = 0
while True:
    print(f"\n--- Inicio paso {paso} ---")
    edificios = ed.edificio()
    print("========== MENÚ ==========")
    print("1. Construir casa")
    print("2. Construir colegio")
    print("3. Construir hospital")
    print("4. Construir museo")
    print("5. Ver edificios construidos")
    print("6. Pedir préstamo")
    print("7. Salir")
    eleccion = input("\nSeleccione una opción: ")
    if eleccion == "1":
        ed.construir(edificios, "Casa")
        paso += 1
    elif eleccion == "2":
        ed.construir(edificios, "Colegio")
        paso += 1
    elif eleccion == "3":
        ed.construir(edificios, "Hospital")
        paso += 1
    elif eleccion == "4":
        ed.construir(edificios, "Museo")
        paso += 1
    elif eleccion == "5":
        ed.mostrar_edificios_registrados()
    elif eleccion == "6":
        ed.pedir_prestamo(paso)
    elif eleccion == "7":
        print("Saliendo del programa...")
        break
    else:
        print("Opción no válida")
    print(f"\n--- Fin paso {paso} ---\n")
    time.sleep(5)
