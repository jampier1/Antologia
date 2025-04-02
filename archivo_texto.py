# Escritura de Archivo de Texto

# Abrimos (o creamos) el archivo my_notes.txt en modo escritura ('w')
with open('my_notes.txt', 'w') as file:
    # Escribimos tres líneas de notas personales en el archivo
    file.write("Nota 1: Hola soy Jampier López.\n")
    file.write("Nota 2: Tengo que estudiar para la semana de examenes.\n")
    file.write("Nota 3: Tengo que terminar los deberes hasta el dia viernes.\n")

# Lectura de Archivo de Texto

# Abrimos el archivo my_notes.txt en modo lectura ('r')
with open('my_notes.txt', 'r') as file:
    # Leemos el contenido del archivo línea por línea
    for line in file:
        # Mostramos cada línea leída en la consola
        print(line.strip())  # strip() se usa para eliminar el salto de línea al final

# No es necesario cerrar el archivo manualmente cuando se usa 'with',
# ya que se cierra automáticamente al salir del bloque.
