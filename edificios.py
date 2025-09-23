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

    casa = [[10, 5, 15, 30], [20, 10, 25, 50], [30, 15, 35, 70]]
    colegio = [[20, 10, 25, 50], [30, 15, 35, 70], [40, 20, 45, 90]]
    hospital = [[30, 20, 40, 100], [40, 25, 50, 120], [50, 30, 60, 150]]
    museo = [[25, 15, 30, 80], [35, 20, 40, 100], [45, 25, 50, 130]]

    subsidio = [[5, 5, 5, 5], [5, 5, 5, 5], [5, 5, 5, 5]]

    casa_subsidio = rm.sumar_matrices(casa, subsidio)
    colegio_subsidio = rm.sumar_matrices(colegio, subsidio)
    hospital_subsidio = rm.sumar_matrices(hospital, subsidio)
    museo_subsidio = rm.sumar_matrices(museo, subsidio)

    def imprimir_costos(nombre, matriz):
        print(f"--- {nombre} ---")
        for i, fila in enumerate(matriz):
            print(f"Tipo {i+1}: ", end="")
            for recurso, valor in zip(nombres, fila):
                print(f"{recurso}: {valor}", end="  ")
            print()
        print()

    print("========== COSTOS DE CONSTRUCCIÓN CON SUBSIDIO ==========")
    imprimir_costos("Casa", casa_subsidio)
    imprimir_costos("Colegio", colegio_subsidio)
    imprimir_costos("Hospital", hospital_subsidio)
    imprimir_costos("Museo", museo_subsidio)

def construir(tipo, categoria):
    global madera, piedra, metal, dinero
    if tipo == "1":
        costos = [[10, 5, 15, 30], [20, 10, 25, 50], [30, 15, 35, 70]]
    elif tipo == "2":
        costos = [[20, 10, 25, 50], [30, 15, 35, 70], [40, 20, 45, 90]]
    elif tipo == "3":
        costos = [[30, 20, 40, 100], [40, 25, 50, 120], [50, 30, 60, 150]]
    else:
        print("Tipo inválido.")
        return

    subsidio = [5, 5, 5, 5]
    costos_categoria = costos[categoria - 1]
    costos_finales = [c + s for c, s in zip(costos_categoria, subsidio)]

    if (madera >= costos_finales[0] and piedra >= costos_finales[1] and
        metal >= costos_finales[2] and dinero >= costos_finales[3]):
        madera -= costos_finales[0]
        piedra -= costos_finales[1]
        metal -= costos_finales[2]
        dinero -= costos_finales[3]
        print("Construcción exitosa.")
    else:
        print("No hay suficientes recursos para construir.")
