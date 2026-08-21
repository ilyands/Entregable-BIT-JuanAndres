
#Registro estudiantes

estudiantes = [
    ("Estefania", 20, 4.5),
    ("Carlos", 21, 3.8),
    ("Laura", 19, 4.2),
    ("Andrés", 22, 2.7),
    ("Sofía", 20, 4.8),
    ("Juan", 23, 3.5),
    ("María", 21, 4.0),
    ("Pedro", 20, 2.9)
]


#Mostrar info

print("== INFORMACIÓN DE LOS ESTUDIANTES ==")

for estudiante in estudiantes:
    nombre = estudiante[0]
    edad = estudiante[1]
    nota = estudiante[2]

    print(f"{nombre} tiene {edad} años y su nota fue {nota}")


#Clasificación

print("\n== CLASIFICACIÓN DE ESTUDIANTES ==")

for estudiante in estudiantes:
    nombre = estudiante[0]
    nota = estudiante[2]

    if nota >= 4.5:
        clasificacion = "Excelente"
    elif nota >= 4.0:
        clasificacion = "Bueno"
    elif nota >= 3.0:
        clasificacion = "Aceptable"
    else:
        clasificacion = "Reprobó"

    print(f"{nombre}: {clasificacion}")


#Promedio

print("\n== PROMEDIO GENERAL ==")

suma_notas = 0

for estudiante in estudiantes:
    suma_notas += estudiante[2]

promedio = suma_notas / len(estudiantes)

print(f"El promedio general es: {promedio:.2f}")


# 5. Búsqueda de estudiante

print("\n== BÚSQUEDA DE ESTUDIANTE ==")

nombre_buscar = input("Ingrese el nombre del estudiante que desea buscar: ")

encontrado = False

for estudiante in estudiantes:
    if estudiante[0].lower() == nombre_buscar.lower():
        encontrado = True
        break

if encontrado:
    print(f"El estudiante {nombre_buscar} fue encontrado.")
else:
    print(f"No se encontró ningún estudiante llamado {nombre_buscar}.")


#Diccionario de ciudades

print("\n===== CIUDAD DE LOS ESTUDIANTES =====")

ciudades = {
    "Ana": "Bogotá",
    "Carlos": "Medellín",
    "Laura": "Bogotá",
    "Andrés": "Cali",
    "Sofía": "Bogotá",
    "Juan": "Pereira",
    "María": "Medellín",
    "Pedro": "Cali"
}

for nombre, ciudad in ciudades.items():
    print(f"{nombre} vive en {ciudad}")


#Cantidad de estudiantes por ciudad

print("\n== CANTIDAD DE ESTUDIANTES POR CIUDAD ==")

cantidad_ciudades = {}

for ciudad in ciudades.values():

    if ciudad in cantidad_ciudades:
        cantidad_ciudades[ciudad] += 1
    else:
        cantidad_ciudades[ciudad] = 1

print(cantidad_ciudades)


#Ciclo While

print("\n== INGRESO DE NÚMEROS ==")

cantidad = 0
suma = 0

while True:
    numero = float(input("Ingrese un número (0 para terminar): "))

    if numero == 0:
        break

    cantidad += 1
    suma += numero

if cantidad > 0:
    promedio_numeros = suma / cantidad
else:
    promedio_numeros = 0

print(f"Cantidad de números ingresados: {cantidad}")
print(f"Suma total: {suma}")
print(f"Promedio: {promedio_numeros}")


#Break y continue

print("\n== BREAK Y CONTINUE ==")

for numero in range(1, 31):

    if numero % 3 == 0:
        continue

    if numero == 25:
        break

    print(numero)