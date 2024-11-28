#Escribe un programa que solicite un número y determine si es mayor o menor que 10.

def mayormenor(): #se apertura función a utilizar
    
    while True: #sentencia repetitiva que nos permitirá repetir el programa hasta que las condiciones se cumplan

        num= int(input("Ingrese un número: \n" ) )#imprime en pantalla la solicitud al usuario y le permite ingresar el número, el mismo que es declarado como una variable entera
        print ("Verificaremos si el número es mayor o menor a 10.") #se imprime en pantalla instrucciones para el usuario
        if (num > 10): #función para verificar si el número es mayor a 10
            print (f"El número {num} es mayor a 10")
        elif (num==10):#función para verificar si el número es igual a 10
            print (f"El número {num} es igual a 10")
        else: #en el caso de ser negativas las dos sentencias anteriores se descarta como menor
            print (f"El número {num} es menor a 10")
        otronum = input("¿Desea ingresar otro número? (S/N): ").upper() #función que permite al usuario decidir si quiere seguir ejecutando el programa
        if otronum != 'S':
            break 

mayormenor() 