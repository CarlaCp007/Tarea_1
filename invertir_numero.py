#Solicita un número entero y calcula la suma de sus dígitos.


num= int(input("Introduce un número entero: "))# Solicitar un número entero al usuario

suma= sum(int(digito) for digito in str(abs(num)))# Convertir el número en una cadena para iterar sobre sus dígitos

print(f"La suma de los dígitos de {num} es: {suma}.") 