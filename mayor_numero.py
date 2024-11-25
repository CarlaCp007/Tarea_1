#Solicita tres números y determina cuál es el mayor.

def mayor(): #se apertura función a utilizar
    
    while True: #sentencia repetitiva que nos permitirá repetir el programa hasta que las condiciones se cumplan

        print ("Ingrese 3 números y verificaremos cual es el mayor.") #se imprime en pantalla instrucciones para el usuario
        num1= int(input("Ingrese el primer número: \n" ) )#imprime en pantalla la solicitud al usuario y le permite ingresar el número, el mismo que es declarado como una variable entera
        num2= int(input("Ingrese el primer número: \n" ) )#imprime en pantalla la solicitud al usuario y le permite ingresar el número, el mismo que es declarado como una variable entera
        num3= int(input("Ingrese el primer número: \n" ) )#imprime en pantalla la solicitud al usuario y le permite ingresar el número, el mismo que es declarado como una variable entera
        if (num1 > num2) and (num1>num3): #función para verificar si el número es mayor a 10
            print (f"El número {num1} es el mayor.")
        elif (num2>num1) and (num2>num3):#función para verificar si el número es igual a 10
            print (f"El número {num2} es el mayor")
        elif (num3>num1) and (num3>num2):#función para verificar si el número es igual a 10
            print (f"El número {num3} es el mayor")
        else: #en el caso de ser negativas las dos sentencias anteriores se descarta como menor
            print (f"Uno de los números se ha repetido, inicie de nuevo el proceso.")
        otronum = input("¿Desea ingresar otro número? (S/N): ").upper() #función que permite al usuario decidir si quiere seguir ejecutando el programa
        if otronum != 'S':
            break 

mayor()