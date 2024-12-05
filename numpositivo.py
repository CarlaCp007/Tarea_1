#Solicita al usuario un número y determina si es positivo, negativo o cero.

def numpositivo(): #se apertura función a utilizar
    
    while True: #sentencia repetitiva que nos permitirá repetir el programa hasta que las condiciones se cumplan

        num= int(input("Ingrese un número: \n" ) )#imprime en pantalla la solicitud al usuario y le permite ingresar el número, el mismo que es declarado como una variable entera
        print ("Verificaremos si el número es positivo o negativo.") #se imprime en pantalla instrucciones para el usuario
        if (num > 0): #función para verificar si el número es positivo
            print (f"El número {num} es positivo")
        elif (num==0):#función para verificar si el número es igual a 0
            print (f"El número {num} es igual a 0")
        else: #en el caso de ser negativas las dos sentencias anteriores se descarta como negativo
            print (f"El número {num} es negativo")
        otronum = input("¿Desea ingresar otro número? (S/N): ").upper() #función que permite al usuario decidir si quiere seguir ejecutando el programa
        if otronum != 'S':
            break 

numpositivo() 