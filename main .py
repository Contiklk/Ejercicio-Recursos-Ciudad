import resource_management as rm
import edificios as ed
import time

paso = 0
while True:
    paso += 1
    print(f"\n--- Inicio paso {paso} ---")
    ed.edificio()
    print("========== MENÚ ==========")
    print("1. Construir casa")
    print("2. Construir colegio")
    print("3. Construir hospital")
    print("4. Construir museo")
    print("5. Salir")
    eleccion = input("\nSeleccione una opción: ")
    if eleccion == "1":
        tipo = input("Elige el tipo de casa (1, 2, 3):")
    elif eleccion == "2":
        tipo = input("Elige el tipo de colegio (1, 2, 3):")
    elif eleccion == "3":
        tipo = input("Elige el tipo de hospital (1, 2, 3):")
    elif eleccion == "4":
        tipo = input("Elige el tipo de museo (1, 2, 3):")
    else:
        break
    print(f"--- Fin paso {paso} ---\n")
    time.sleep(3)
