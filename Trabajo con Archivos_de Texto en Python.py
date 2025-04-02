# Programa para trabajar con archivos
# Tarea de Python

# Parte 1: Escribir en un archivo
print("Escribiendo notas en el archivo...")
archivo = open("my_notes.txt", "w")

# Escribo mis notas
archivo.write("Tengo examen de matemáticas el jueves\n")
archivo.write("Recordar llamar a Juan para el trabajo grupal\n")
archivo.write("Comprar comida para mi perro\n")

# Cierro el archivo
archivo.close()
print("Archivo creado")

# Parte 2: Leer el archivo
print("\nLeyendo mis notas:")
archivo = open("my_notes.txt", "r")

# Leo línea por línea
linea = archivo.readline()
while linea:
    print(linea, end="")
    linea = archivo.readline()

# Cierro el archivo otra vez
archivo.close()
print("\nFin del programa")