import resource_management as rm

madera = 450
piedra = 350
metal = 400
dinero = 1000

def edificio():
    recursos = [madera, piedra, metal, dinero]
    nombres = ["Madera", "Piedra", "Metal", "Dinero"]
    total_recursos = rm.sumar_array(recursos)

    print("\n========== RECURSOS DISPONIBLES ==========")
    for nombre, valor in zip(nombres, recursos):
        print(f"{nombre}: {valor}")
    print(f"Total de recursos: {total_recursos}\n")

    edificios = {
        "Casa": {
            "costos": [[10, 5, 15, 30]],
            "tiempo": 120
        },
        "Colegio": {
            "costos": [[20, 10, 25, 50]],
            "tiempo": 200
        },
        "Hospital": {
            "costos": [[30, 20, 40, 100]],
            "tiempo": 400
        },
        "Museo": {
            "costos": [[25, 15, 30, 80]],
            "tiempo": 300
        }
    }

    subsidio = [[5, 5, 5, 5]]

    edificios["Casa"]["costos"] = rm.sumar_matrices(edificios["Casa"]["costos"], subsidio)
    edificios["Colegio"]["costos"] = rm.sumar_matrices(edificios["Colegio"]["costos"], subsidio)
    edificios["Hospital"]["costos"] = rm.sumar_matrices(edificios["Hospital"]["costos"], subsidio)
    edificios["Museo"]["costos"] = rm.sumar_matrices(edificios["Museo"]["costos"], subsidio)

    print("========== COSTOS DE CONSTRUCCIÓN CON SUBSIDIO ==========")
    for nombre_edificio, datos in edificios.items():
        print(f"--- {nombre_edificio} ---")
        for fila in datos["costos"]:
            for recurso, valor in zip(nombres, fila):
                print(f"{recurso}: {valor}", end="  ")
            print()
        print()
    return edificios

def construir(edificios, nombre_edificio, categoria=1):
    global madera, piedra, metal, dinero
    if nombre_edificio not in edificios:
        print("Edificio inválido.")
        return

    datos = edificios[nombre_edificio]
    costos = datos["costos"]

    if categoria < 1 or categoria > len(costos):
        print("Categoría inválida.")
        return

    obreros = int(input("Número de obreros disponibles: "))
    print("Seleccione el modo de construcción:")
    print("1. Equitativo")
    print("2. Exclusivo")
    print("3. Grupos")
    eleccion = input("Opción: ")
    if eleccion == "1":
        modo = "equitativo"
    elif eleccion == "2":
        modo = "exclusivo"
    elif eleccion == "3":
        modo = "grupos"
    else:
        print("Opción no válida, se usará 'equitativo'")
        modo = "equitativo"

    grupo = 2
    if modo == "grupos":
        grupo = int(input("Tamaño del grupo de obreros: "))

    # Simulamos solo el edificio elegido

    tiempo = simular_tiempo({nombre_edificio: edificios[nombre_edificio]}, obreros, modo, grupo)
    print(f"\nConstrucción de {nombre_edificio} terminada en {tiempo} horas con modo '{modo}'.\n")
    registrar_edificio(nombre_edificio)

    costos_finales = costos[categoria - 1]

    if (madera >= costos_finales[0] and piedra >= costos_finales[1] and
        metal >= costos_finales[2] and dinero >= costos_finales[3]):
        madera -= costos_finales[0]
        piedra -= costos_finales[1]
        metal -= costos_finales[2]
        dinero -= costos_finales[3]
        print("Construcción exitosa.")
    else:
        print("No hay suficientes recursos para construir.")

edificios_construidos = []

def registrar_edificio(nombre):
    edificios_construidos.append(nombre)

def mostrar_edificios_registrados():
    print("\n--- EDIFICIOS CONSTRUIDOS ---")
    if edificios_construidos:
        for i, nombre in enumerate(edificios_construidos, 1):
            print(f"{i}. {nombre}")
    else:
        print("No se ha construido ningún edificio aún.")

def simular_tiempo(edificios, obreros, modo="equitativo", grupo=2):
    tiempos = {nombre: datos["tiempo"] for nombre, datos in edificios.items()}
    tiempo_total = 0

    while any(t > 0 for t in tiempos.values()):
        tiempo_total += 1

        if modo == "equitativo":
            activos = [n for n, t in tiempos.items() if t > 0]
            if activos:
                obreros_por_obra = max(1, obreros // len(activos))
                for n in activos:
                    tiempos[n] = max(0, tiempos[n] - obreros_por_obra)

        elif modo == "exclusivo":
            activos = [n for n, t in tiempos.items() if t > 0]
            for n in activos[:obreros]:
                tiempos[n] = max(0, tiempos[n] - 1)

        elif modo == "grupos":
            activos = [n for n, t in tiempos.items() if t > 0]
            max_obras = obreros // grupo
            for n in activos[:max_obras]:
                tiempos[n] = max(0, tiempos[n] - grupo)

        else:
            raise ValueError("Modo no reconocido")

    return tiempo_total

ultimo_prestamo = 0

def pedir_prestamo(paso_actual):
    global madera, piedra, metal, dinero, ultimo_prestamo
    if paso_actual - ultimo_prestamo >= 5 and paso_actual >= 5:
        madera += 200
        piedra += 200
        metal += 200
        dinero += 200
        ultimo_prestamo = paso_actual
        print("\n¡Préstamo recibido! +200 de cada recurso.")
    else:
        if paso_actual < 5:
            print("\nNo puedes pedir un préstamo antes del paso 5.")
        else:
            faltan = 5 - (paso_actual - ultimo_prestamo)
            print(f"\nNo puedes pedir otro préstamo aún. Debes esperar {faltan} paso(s) más.")
