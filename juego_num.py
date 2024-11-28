#Genera un número aleatorio entre 1 y 10 y solicita al usuario que adivine el número. Usa if para verificar si acertó o no.

import random

def juego():

    while True: #sentencia repetitiva que nos permitirá repetir el programa hasta que las condiciones se cumplan

        num1=random.randint(1, 10)
        print ("Estoy pensando un número,¿lo adivinas?") #se imprime en pantalla instrucciones para el usuario
        num= int(input("Ingrese el número: \n" ) )#imprime en pantalla la solicitud al usuario y le permite ingresar el número, el mismo que es declarado como una variable entera
        if (num==num1):#función para verificar si el número es igual a 10
            print (f"¡Felicidades, acertaste!")
        else: #en el caso de ser negativas las dos sentencias anteriores se descarta como menor
            print (f"Intenta de nuevo.")
            num= int(input("Ingrese el número: \n" ) )
            while (num!=num1):
                print (f"Intenta de nuevo.")
                num= int(input("Ingrese el número: \n" ) )
            else:
                print (f"¡Felicidades, acertaste!")
        otronum = input("¿Deseas jugar de nuevo? (S/N): ").upper() #función que permite al usuario decidir si quiere seguir ejecutando el programa
        if otronum != 'S':
            break 

juego()