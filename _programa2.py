# Función para ordenar una fila específica de la matriz
def ordenar_fila(matriz, fila):
    if 0 <= fila < len(matriz):
        matriz[fila].sort()
    return matriz

matriz = [
    [9, 4, 7],
    [2, 6, 1],
    [5, 8, 3]
]

fila_ordenar = 1

print("Matriz original:")
for fila in matriz:
    print(fila)

matriz_ordenada = ordenar_fila(matriz, fila_ordenar)
print("\nMatriz con la fila ordenada:")
for fila in matriz_ordenada:
    print(fila)
