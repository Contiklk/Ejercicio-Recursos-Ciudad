import resource_management as rm
import math
import time

# RECURSOS Y EDIFICIOS

def edificio():
    madera = 450
    piedra = 350
    metal = 400
    dinero = 1000

    total_recursos = rm.sumar_array([madera, piedra, metal, dinero])
    print(f"Total de recursos: {total_recursos}")

    # Matrices de recursos (ahora añadimos coste en tiempo por obrero [horas])
    casa = {"recursos": [[10, 5, 15, 30], [20, 10, 25, 50], [30, 15, 35, 70]],
            "tiempo": 120}
    colegio = {"recursos": [[20, 10, 25, 50], [30, 15, 35, 70], [40, 20, 45, 90]],
               "tiempo": 200}
    hospital = {"recursos": [[30, 20, 40, 100], [40, 25, 50, 120], [50, 30, 60, 150]],
                "tiempo": 400}
    museo = {"recursos": [[25, 15, 30, 80], [35, 20, 40, 100], [45, 25, 50, 130]],
             "tiempo": 300}

    subsidio = [[5, 5, 5, 5], [5, 5, 5, 5], [5, 5, 5, 5]]
 
    casa["recursos"] = rm.sumar_matrices(casa["recursos"], subsidio)
    colegio["recursos"] = rm.sumar_matrices(colegio["recursos"], subsidio)
    hospital["recursos"] = rm.sumar_matrices(hospital["recursos"], subsidio)
    museo["recursos"] = rm.sumar_matrices(museo["recursos"], subsidio)

    return {"Casa": casa, "Colegio": colegio, "Hospital": hospital, "Museo": museo}

# SIMULACIONES DE TIEMPO

def simular_tiempo(edificios, obreros, modo="equitativo", grupo=2):
    
    "Simula el tiempo de construcción de varias obras con diferentes estrategias.Equitativo, exclusivo y grupos."

    tiempos = {nombre: datos["tiempo"] for nombre, datos in edificios.items()}
    tiempo_total = 0

    while any(t > 0 for t in tiempos.values()):
        tiempo_total += 1

        if modo == "equitativo":
            # Obreros repartidos entre todas las obras
            activos = [n for n, t in tiempos.items() if t > 0]
            if activos:
                obreros_por_obra = max(1, obreros // len(activos))
                for n in activos:
                    tiempos[n] = max(0, tiempos[n] - obreros_por_obra)

        elif modo == "exclusivo":
            # Solo un obrero por obra
            activos = [n for n, t in tiempos.items() if t > 0]
            for n in activos[:obreros]:  # Solo trabajan tantos obreros como obras disponibles
                tiempos[n] = max(0, tiempos[n] - 1)

        elif modo == "grupos":
            # Los obreros se organizan en grupos
            activos = [n for n, t in tiempos.items() if t > 0]
            max_obras = obreros // grupo
            for n in activos[:max_obras]:
                tiempos[n] = max(0, tiempos[n] - grupo)

        else:
            raise ValueError("Modo no reconocido")

    return tiempo_total

# MENÚ

def menu():
    edificios = edificio()
    while True:
        print("\n--- MENÚ ---")
        print("1. Construir casa")
        print("2. Construir colegio")
        print("3. Construir hospital")
        print("4. Construir museo")
        print("5. Simular tiempos")
        print("6. Salir")
        eleccion = input("Seleccione una opción: ")

        if eleccion == "1":
            print(edificios["Casa"])
        elif eleccion == "2":
            print(edificios["Colegio"])
        elif eleccion == "3":
            print(edificios["Hospital"])
        elif eleccion == "4":
            print(edificios["Museo"])
        elif eleccion == "5":
            obreros = int(input("Número de obreros: "))
            print("Simulación en modo 'equitativo':", simular_tiempo(edificios, obreros, "equitativo"))
            print("Simulación en modo 'exclusivo':", simular_tiempo(edificios, obreros, "exclusivo"))
            print("Simulación en modo 'grupos':", simular_tiempo(edificios, obreros, "grupos", grupo=2))
        elif eleccion == "6":
            break
        else:
            print("Opción no válida")
menu()

