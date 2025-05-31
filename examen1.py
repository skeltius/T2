import random
import math

def distancia(punto):
    x, y = punto
    return math.sqrt(x**2 + y**2)

def divide_y_venceras(coordenadas):
    if len(coordenadas) == 1:
        return coordenadas[0] if coordenadas[0][0] > 0 and coordenadas[0][1] < 0 else None

    mid = len(coordenadas) // 2
    izquierda = divide_y_venceras(coordenadas[:mid])
    derecha = divide_y_venceras(coordenadas[mid:])

    if izquierda is not None and derecha is not None:
        return izquierda if distancia(izquierda) > distancia(derecha) else derecha
    return izquierda if izquierda is not None else derecha

n = int(input("Ingrese la cantidad de pares de coordenadas: "))

coordenadas = [[random.randint(-81, 81), random.randint(-81, 81)] for _ in range(n)]

print("Coordenadas generadas:")
for coord in coordenadas:
    print(coord)

resultado = divide_y_venceras(coordenadas)

if resultado is not None:
    print(f"La coordenada más alejada del origen (0,0) con X positivo e Y negativo es: {resultado} con distancia {distancia(resultado):.2f}")
else:
    print("No se encontró ninguna coordenada que cumpla con las condiciones.")

