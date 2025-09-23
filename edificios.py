import resource_management as rm

def edificio():
    madera = 450
    piedra = 350
    metal = 400
    dinero = 1000

    total_recursos = rm.sumar_array([madera, piedra, metal, dinero])
    print(f"Total de recursos: {total_recursos}")

    casa = [[10, 5, 15, 30], [20, 10, 25, 50], [30, 15, 35, 70]]
    colegio = [[20, 10, 25, 50], [30, 15, 35, 70], [40, 20, 45, 90]]
    hospital = [[30, 20, 40, 100], [40, 25, 50, 120], [50, 30, 60, 150]]
    museo = [[25, 15, 30, 80], [35, 20, 40, 100], [45, 25, 50, 130]]

    subsidio = [[5, 5, 5, 5], [5, 5, 5, 5], [5, 5, 5, 5]]

    casa_subsidio = rm.sumar_matrices(casa, subsidio)
    colegio_subsidio = rm.sumar_matrices(colegio, subsidio)
    hospital_subsidio = rm.sumar_matrices(hospital, subsidio)
    museo_subsidio = rm.sumar_matrices(museo, subsidio)

    print(f"Costo de construcción de casa con subsidio: {casa_subsidio}")
    print(f"Costo de construcción de colegio con subsidio: {colegio_subsidio}")
    print(f"Costo de construcción de hospital con subsidio: {hospital_subsidio}")
    print(f"Costo de construcción de museo con subsidio: {museo_subsidio}")
