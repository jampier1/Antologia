# Crear un diccionario inicial con información personal
informacion_personal = {
    "nombre": "Darwin Jeampierre",
    "apellido": "López Cholango",
    "edad": 25,
    "ciudad": "Cayambe",
    "profesion": "Estudiante de Tics"
}

# Modificar el valor de la ciudad
informacion_personal["ciudad"] = "Cayambe"

# Verificar si existe la clave "telefono" y agregarla si no existe
if "telefono" not in informacion_personal:
    informacion_personal["telefono"] = "+593 97 977 9126"

# Eliminar la clave "edad"
del informacion_personal["edad"]

# Imprimir el diccionario final
print("Información personal actualizada:")
for clave, valor in informacion_personal.items():
    print(f"{clave}: {valor}")