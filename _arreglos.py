# Función para buscar un número en la matriz
def buscar_en_matriz(matriz, valor):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == valor:
                return (i,j)
    return None

matriz = [
    [4, 7, 1],
    [8, 3, 9],
    [2, 6, 5]
]

valor_buscado= 6
resultado = buscar_en_matriz(matriz, valor_buscado)
if resultado:
    print(f"valor {valor_buscado} encontrado en la posición {resultado}.")
else:
    print(f"valor {valor_buscado} no encontrado en la matriz.")