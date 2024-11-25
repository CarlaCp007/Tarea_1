#Escribe un programa que solicite un número y determine si es mayor o menor que 10.

def mayormenor(): #se apertura función a utilizar
    
    while True: #sentencia repetitiva que nos permitirá repetir el programa hasta que las condiciones se cumplan

        num= int(input("Ingrese un número: \n" ) )#imprime en pantalla la solicitud al usuario y le permite ingresar el número
        print ("Verificaremos si el número es mayor o menor a 10.") #se imprime en pantalla instrucciones para el usuario
        if (num > 10): #condicional para verificar si el 
            print (f"El número {num} es mayor a 10")
        else:
            print (f"El número {num} es menor a 10")
        otronum = input("¿Desea ingresar otro número? (S/N): ").upper()
        if otronum != 'S':
            break

mayormenor()