import re
from excepciones import OpcionNoValidaError, NombreError, DNIError

personas = []

def mostrar_menu():
    print("\nMenú de opciones:")
    print("1.- Crear persona")
    print("2.- Cargar personas por defecto")
    print("3.- Mostrar todas las personas")
    print("4.- Mostrar personas de una ciudad")
    print("5.- Dibujar histograma por ciudades")
    print("6.- Salir")
    
    opcion = input("Elige una opción: ")
    if not opcion.isdigit():
        raise OpcionNoValidaError("Introduce un número")
    opcion = int(opcion)
    if opcion < 1 or opcion > 6:
        raise OpcionNoValidaError("La opción debe estar entre 1 y 6")
    return opcion

def validar_nombre(nombre):
    if not re.match(r"^[A-Z][a-z]+$", nombre):
        raise NombreError("El nombre debe tener formato: Aaaaaa")

def validar_dni(dni):
    if not re.match(r"^\d{2}[A-Z]$", dni):
        raise DNIError("El formato del DNI debe ser: dos dígitos seguidos de una letra.")
    digitos = int(dni[:2])
    letra_correcta = chr(65 + sum(map(int, str(digitos))))
    if dni[2] != letra_correcta:
        raise DNIError(f"Letra incorrecta. La letra debería ser {letra_correcta}")

def crear_personas():
    nombre = input("Introduce el nombre: ")
    validar_nombre(nombre)
    dni = input("Introduce el DNI: ")
    validar_dni(dni)
    ciudad = input("Introduce la ciudad: ")
    personas.append({"nombre": nombre, "dni": dni, "ciudad": ciudad})
    print(f"Persona {nombre} creada con éxito.")

def cargar_personas_por_defecto():
    global personas
    personas.extend([
        {"nombre": "Ana", "dni": "11C", "ciudad": "Madrid"},
        {"nombre": "Luis", "dni": "22F", "ciudad": "Barcelona"},
        {"nombre": "Elena", "dni": "33I", "ciudad": "Madrid"}
    ])
    print("Personas cargadas por defecto.")

def mostrar_todas_personas():
    if not personas:
        print("No hay personas registradas.")
    else:
        for p in personas:
            print(f"Nombre: {p['nombre']}, DNI: {p['dni']}, Ciudad: {p['ciudad']}")

def mostrar_personas_ciudad():
    ciudad = input("Introduce el nombre de la ciudad: ")
    personas_ciudad = [p for p in personas if p['ciudad'] == ciudad]
    if not personas_ciudad:
        print(f"No hay personas registradas en {ciudad}.")
    else:
        for p in personas_ciudad:
            print(f"Nombre: {p['nombre']}, DNI: {p['dni']}")

def dibujar_histograma():
    if not personas:
        print("No hay datos para mostrar un histograma.")
    else:
        ciudades = {}
        for p in personas:
            ciudades[p['ciudad']] = ciudades.get(p['ciudad'], 0) + 1
        print("\nHistograma de personas por ciudad:")
        for ciudad, count in ciudades.items():
            print(f"{ciudad}: {'*' * count}")
