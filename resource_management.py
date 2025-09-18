def modulo(a, b):
    int = a // b
    resto = a - int * b
    return resto

def raiz(a):
    x = 0
    while x*x <= a:
        x = x+1
    return x-1

def potencia(base, exp):
    i = 1
    for x in range(exp):
        i = i * base
    return i

def ordenar_array(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

def sumar_array(arr):
    total = 0
    for x in arr:
        total += x
    return total

def sumar_matrices(matriz1, matriz2):
    if len(matriz1) != len(matriz2) or any(len(f1) != len(f2) for f1, f2 in zip(matriz1, matriz2)):
        raise ValueError("Las matrices deben tener el mismo tamaño")
    return [[f1[i] + f2[i] for i in range(len(f1))] for f1, f2 in zip(matriz1, matriz2)]
