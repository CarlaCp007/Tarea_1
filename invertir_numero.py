#Solicita un número entero y muestra su versión invertida.

try:
    numero = int(input("Ingrese un número entero: "))
    
    # Convertir el número a cadena, invertirlo y preservar el signo
    if numero < 0:
        numero_invertido = int("-" + str(abs(numero))[::-1])
    else:
        numero_invertido = int(str(numero)[::-1])
    
    print(f"El número invertido es: {numero_invertido}")
except ValueError:
    print("Por favor, ingrese un número entero válido.")