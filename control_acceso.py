#Solicita un nombre de usuario y contraseña, y valida si ambos son correctos. Permite tres intentos antes de bloquear el acceso.

def control(): #se apertura función a utilizar
    
    while True: #sentencia repetitiva que nos permitirá repetir el programa hasta que las condiciones se cumplan

        contra=12345
        usuario="admin"
        contador=1
        user= str(input("Ingrese el usuario: \n" ) ).lower()#imprime en pantalla la solicitud al usuario y le permite ingresar el número, el mismo que es declarado como una variable entera
        num= int(input("Ingrese la contraseña: \n" ) )#imprime en pantalla la solicitud al usuario y le permite ingresar el número, el mismo que es declarado como una variable entera  
        while(contador!=3):
            contador=contador+1
            if (num == contra) and (user==usuario): #función para verificar si el número es mayor a 10
                print (f"Acceso concedido.")
                break
            else: #en el caso de ser negativas las dos sentencias anteriores se descarta como menor
                print (f"Acceso denegado. \nIntente nuevamente.")
                user= str(input("Ingrese el usuario: \n" ) ).lower()#imprime en pantalla la solicitud al usuario y le permite ingresar el número, el mismo que es declarado como una variable entera
                num= int(input("Ingrese la contraseña: \n" ) )#imprime en pantalla la solicitud al usuario y le permite ingresar el número, el mismo que es declarado como una variable entera  
        else:
            print("Acceso bloqueado.")
            break
        otronum = input("¿Desea ingresar otra vez? (S/N): ").upper() #función que permite al usuario decidir si quiere seguir ejecutando el programa
        if otronum != 'S':
            break 

control() 