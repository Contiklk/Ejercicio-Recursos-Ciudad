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
