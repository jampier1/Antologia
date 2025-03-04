# Definir las dimensiones de la matriz
ciudades = ['Quito', 'El Coca', 'Esmeraldas']
dias_semana = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo']
semanas = 4

# Matriz 3D para almacenar las temperaturas
temperaturas = [[[0 for _ in range(len(dias_semana))] for _ in range(semanas)] for _ in range(len(ciudades))]

# Función para ingresar datos de temperaturas
def ingresar_temperaturas():
    for i in range(len(ciudades)):
        print(f"\nIngresar temperaturas para {ciudades[i]}:")
        for j in range(semanas):
            print(f"\nSemana {j + 1}:")
            for k in range(len(dias_semana)):
                temperatura = float(input(f"Temperatura para {dias_semana[k]}: "))
                temperaturas[i][j][k] = temperatura

# Función para calcular el promedio de temperaturas por ciudad y semana
def calcular_promedios():
    promedios = [[0 for _ in range(semanas)] for _ in range(len(ciudades))]
    for i in range(len(ciudades)):
        for j in range(semanas):
            suma_temperaturas = sum(temperaturas[i][j])
            promedio = suma_temperaturas / len(dias_semana)
            promedios[i][j] = promedio
    return promedios

# Función para mostrar los promedios de temperaturas
def mostrar_promedios(promedios):
    print("\nPromedios de temperaturas por ciudad y semana:")
    for i in range(len(ciudades)):
        for j in range(semanas):
            print(f"Promedio en {ciudades[i]} para la semana {j + 1}: {promedios[i][j]:.2f}°C")

# Menú principal de la aplicación
def menu():
    while True:
        print("\n--- Aplicación de Rastreo de Temperaturas ---")
        print("1. Ingresar temperaturas")
        print("2. Calcular promedios")
        print("3. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            ingresar_temperaturas()
        elif opcion == "2":
            promedios = calcular_promedios()
            mostrar_promedios(promedios)
        elif opcion == "3":
            print("Saliendo de la aplicación...")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

menu()
