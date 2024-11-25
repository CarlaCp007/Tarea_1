#Solicita la edad del usuario y determina si es elegible para votar (mayor o igual a 18 años).

def edadvotar(): #se apertura función a utilizar
    
    while True: #sentencia repetitiva que nos permitirá repetir el programa hasta que las condiciones se cumplan

        print ("Verificaremos si usted puede participar en estas votaciones.") #se imprime en pantalla instrucciones para el usuario
        num= int(input("Ingrese su edad: \n" ) )#imprime en pantalla la solicitud al usuario y le permite ingresar el número, el mismo que es declarado como una variable entera
        if (num >= 18): #función para verificar si el número es mayor a 10
            print (f"Usted puede votar.")
        else: #en el caso de ser negativas las dos sentencias anteriores se descarta como menor
            print (f"No puede votar.")
        otronum = input("¿Desea verificar de otra persona? (S/N): ").upper() #función que permite al usuario decidir si quiere seguir ejecutando el programa
        if otronum != 'S':
            break 

edadvotar() 