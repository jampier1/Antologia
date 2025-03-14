temperaturas = [
    [  # Ciudad 1 QUITO
        [  # Semana 1
            {"day": "Lunes", "temp": 15},
            {"day": "Martes", "temp": 16},
            {"day": "Miércoles", "temp": 8},
            {"day": "Jueves", "temp": 7},
            {"day": "Viernes", "temp": 8},
            {"day": "Sábado", "temp": 8},
            {"day": "Domingo", "temp": 9}
        ],
        [  # Semana 2
            {"day": "Lunes", "temp": 11},
            {"day": "Martes", "temp": 12},
            {"day": "Miércoles", "temp": 13},
            {"day": "Jueves", "temp": 14},
            {"day": "Viernes", "temp": 14},
            {"day": "Sábado", "temp": 12},
            {"day": "Domingo", "temp": 11}
        ],
        [  # Semana 3
            {"day": "Lunes", "temp": 20},
            {"day": "Martes", "temp": 14},
            {"day": "Miércoles", "temp": 16},
            {"day": "Jueves", "temp": 23},
            {"day": "Viernes", "temp": 25},
            {"day": "Sábado", "temp": 15},
            {"day": "Domingo", "temp": 18}
        ],
        [  # Semana 4
            {"day": "Lunes", "temp": 18},
            {"day": "Martes", "temp": 19},
            {"day": "Miércoles", "temp": 16},
            {"day": "Jueves", "temp": 14},
            {"day": "Viernes", "temp": 14},
            {"day": "Sábado", "temp": 18},
            {"day": "Domingo", "temp": 16}
        ]
    ],
    [  # Ciudad 2 EL ORO
        [  # Semana 1
            {"day": "Lunes", "temp": 28},
            {"day": "Martes", "temp": 29},
            {"day": "Miércoles", "temp": 20},
            {"day": "Jueves", "temp": 28},
            {"day": "Viernes", "temp": 33},
            {"day": "Sábado", "temp": 33},
            {"day": "Domingo", "temp": 29}
        ],
        [  # Semana 2
            {"day": "Lunes", "temp": 23},
            {"day": "Martes", "temp": 26},
            {"day": "Miércoles", "temp": 30},
            {"day": "Jueves", "temp": 32},
            {"day": "Viernes", "temp": 35},
            {"day": "Sábado", "temp": 27},
            {"day": "Domingo", "temp": 31}
        ],
        [  # Semana 3
            {"day": "Lunes", "temp": 31},
            {"day": "Martes", "temp": 25},
            {"day": "Miércoles", "temp": 28},
            {"day": "Jueves", "temp": 30},
            {"day": "Viernes", "temp": 32},
            {"day": "Sábado", "temp": 26},
            {"day": "Domingo", "temp": 30}
        ],
        [  # Semana 4
            {"day": "Lunes", "temp": 34},
            {"day": "Martes", "temp": 27},
            {"day": "Miércoles", "temp": 29},
            {"day": "Jueves", "temp": 31},
            {"day": "Viernes", "temp": 24},
            {"day": "Sábado", "temp": 27},
            {"day": "Domingo", "temp": 30}
        ]
    ],
    [  # Ciudad 3 ESMERALDAS
        [  # Semana 1
            {"day": "Lunes", "temp": 20},
            {"day": "Martes", "temp": 32},
            {"day": "Miércoles", "temp": 34},
            {"day": "Jueves", "temp": 21},
            {"day": "Viernes", "temp": 28},
            {"day": "Sábado", "temp": 35},
            {"day": "Domingo", "temp": 32}
        ],
        [  # Semana 2
            {"day": "Lunes", "temp": 29},
            {"day": "Martes", "temp": 31},
            {"day": "Miércoles", "temp": 33},
            {"day": "Jueves", "temp": 30},
            {"day": "Viernes", "temp": 27},
            {"day": "Sábado", "temp": 24},
            {"day": "Domingo", "temp": 31}
        ],
        [  # Semana 3
            {"day": "Lunes", "temp": 31},
            {"day": "Martes", "temp": 23},
            {"day": "Miércoles", "temp": 25},
            {"day": "Jueves", "temp": 32},
            {"day": "Viernes", "temp": 29},
            {"day": "Sábado", "temp": 26},
            {"day": "Domingo", "temp": 23}
        ],
        [  # Semana 4
            {"day": "Lunes", "temp": 28},
            {"day": "Martes", "temp": 30},
            {"day": "Miércoles", "temp": 22},
            {"day": "Jueves", "temp": 29},
            {"day": "Viernes", "temp": 26},
            {"day": "Sábado", "temp": 33},
            {"day": "Domingo", "temp": 30}
        ]
    ]
]


# Función que calcula el promedio de temperatura para cada ciudad
def calcular_promedio_ciudad(temperaturas):
    # Lista de nombres de las ciudades
    ciudades = ["Ciudad 1 QUITO", "Ciudad 2 EL ORO", "Ciudad 3 ESMERALDAS"]

    # Diccionario para almacenar los promedios de cada ciudad
    promedios = {}

    # Recorremos cada ciudad en la lista de temperaturas
    for ciudad_idx, ciudad in enumerate(temperaturas):
        # Suma total de las temperaturas de todos los días de todas las semanas
        total_temp = sum(dia["temp"] for semana in ciudad for dia in semana)

        # Contamos el total de días (el número de días de todas las semanas)
        total_dias = sum(len(semana) for semana in ciudad)

        # Calculamos el promedio de las temperaturas
        promedio = total_temp / total_dias if total_dias > 0 else 0

        # Almacenamos el promedio en el diccionario
        promedios[ciudades[ciudad_idx]] = round(promedio, 2)

    # Devolvemos el diccionario con los promedios
    return promedios


# Llamada a la función y almacenamiento de los resultados
promedios = calcular_promedio_ciudad(temperaturas)

# Imprimimos los resultados de los promedios
for ciudad, promedio in promedios.items():
    print(f"Temperatura promedio en {ciudad}: {promedio} grados")
