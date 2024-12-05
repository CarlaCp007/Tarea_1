def es_par(numero):
    """
    Determina si un número es par.
    
    Args:
        numero (int): El número a evaluar.
    
    Returns:
        bool: True si el número es par, False si es impar.

    """
    return numero % 2 == 0

# Ejemplo de uso
try:
    numero = int(input("Ingresa un número: "))
    print(es_par(4))
except ValueError:
    print("Por favor, ingresa un número válido.")