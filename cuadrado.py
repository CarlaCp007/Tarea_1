def calcular_cuadrado(numero):
    """
    Calcula el cuadrado de un número.
    
    Args:
        numero (int o float): El número al que se le calculará el cuadrado.
    
    Returns:
        int o float: El cuadrado del número ingresado.
    """
    return numero ** 2

# Ejemplo de uso
numero = int(input("Ingresa un número para calcular su cuadrado: "))
print(f"El cuadrado de {numero} es {calcular_cuadrado(numero)}.")
