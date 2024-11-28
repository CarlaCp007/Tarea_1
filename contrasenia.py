#Escribe un programa que solicite una contraseña y valide si es correcta (ejemplo: contraseña fija es 12345).

def contrasenia(): #se apertura función a utilizar
    
    while True: #sentencia repetitiva que nos permitirá repetir el programa hasta que las condiciones se cumplan

        contra=12345
        num= int(input("Ingrese la contraseña: \n" ) )#imprime en pantalla la solicitud al usuario y le permite ingresar el número, el mismo que es declarado como una variable entera
        if (num == contra): #función para verificar si el número es mayor a 10
            print (f"Acceso concedido.") #imprime en pantalla el mensaje al usuario
        else: #en el caso de ser negativas las dos sentencias anteriores se descarta como menor
            print (f"Acceso denegado.") #imprime en pantalla el mensaje al usuario
            break
        otronum = input("¿Desea ingresar otra vez? (S/N): ").upper() #función que permite al usuario decidir si quiere seguir ejecutando el programa
        if otronum != 'S': #función que da paso a cerrar el programa en caso de que el usuario haya ingresado otra letra
            break #sentencia que cierra la sentencia while

contrasenia() 