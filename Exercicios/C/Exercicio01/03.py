import math

def calcular_distancia():
    print("Digite as coordenadas dos dois pontos:")
    
    x1 = float(input("x1: "))
    y1 = float(input("y1: "))
    x2 = float(input("x2: "))
    y2 = float(input("y2: "))
    
    distancia = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    
    print(f"\nA distância entre os pontos é: {distancia:.2f}")

calcular_distancia()
