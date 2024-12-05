import math

def calcular_area_circulo(radio):
    """
    Calcula el área de un círculo dado su radio.
    
    Args:
        radio (float): El radio del círculo.
    
    Returns:
        float: El área del círculo.
    """
    if radio < 0:
        raise ValueError("El radio no puede ser negativo.")
    return math.pi * (radio ** 2)

# Ejemplo de uso
try:
    radio = float(input("Ingresa el radio del círculo: "))
    area = calcular_area_circulo(radio)
    print(f"El área del círculo con radio {radio} es {area:.2f}.")
except ValueError as e:
    print(f"Error: {e}")
