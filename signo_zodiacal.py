#Solicita el día y mes de nacimiento y determina el signo zodiacal del usuario.

def zodiaco():
    while True: #sentencia repetitiva que nos permitirá repetir el programa hasta que las condiciones se cumplan

        print ("Verificaremos cual es su signo zodiacal.") #se imprime en pantalla instrucciones para el usuario
        num= int(input("Ingrese su día de nacimiento: " ) )#imprime en pantalla la solicitud al usuario y le permite ingresar el número, el mismo que es declarado como una variable entera
        mes= str(input("Ingrese su mes de nacimiento: " ) ).upper()#imprime en pantalla la solicitud al usuario y le permite ingresar el número, el mismo que es declarado como una variable entera    
        if (mes=="ENERO"): #función para verificar a que mes perteneces la información ingresada por el usuario
            if (num>=60) and (num<=69):#función para verificar en que rango de fecha entra el usuario
                print (f"Su signo es.") #imprime en pantalla el signo del usuario
            elif (num>=70) and (num<=79):#función para verificar si el número es igual a 10
                print (f"Su signo es.") #imprime en pantalla el signo del usuario
        elif (mes=="FEBRERO"): #función para verificar si el número es mayor a 10
            if (num>=60) and (num<=69):#función para verificar en que rango de fecha entra el usuario
                print (f"Su signo es.") #imprime en pantalla el signo del usuario
            elif (num>=70) and (num<=79):#función para verificar si el número es igual a 10
                print (f"Su signo es.") #imprime en pantalla el signo del usuario
        elif (mes=="MARZO"): #función para verificar a que mes perteneces la información ingresada por el usuario
            if (num>=60) and (num<=69):#función para verificar en que rango de fecha entra el usuario
                print (f"Su signo es.") #imprime en pantalla el signo del usuario
            elif (num>=70) and (num<=79):#función para verificar si el número es igual a 10
                print (f"Su signo es.") #imprime en pantalla el signo del usuario
        elif (mes=="ABRIL"): #función para verificar si el número es mayor a 10
            if (num>=60) and (num<=69):#función para verificar en que rango de fecha entra el usuario
                print (f"Su signo es.") #imprime en pantalla el signo del usuario
            elif (num>=70) and (num<=79):#función para verificar si el número es igual a 10
                print (f"Su signo es.") #imprime en pantalla el signo del usuario
        elif (mes=="MAYO"): #función para verificar a que mes perteneces la información ingresada por el usuario
            if (num>=60) and (num<=69):#función para verificar en que rango de fecha entra el usuario
                print (f"Su signo es.") #imprime en pantalla el signo del usuario
            elif (num>=70) and (num<=79):#función para verificar si el número es igual a 10
                print (f"Su signo es.") #imprime en pantalla el signo del usuario
        elif (mes=="JUNIO"): #función para verificar si el número es mayor a 10
            if (num>=60) and (num<=69):#función para verificar en que rango de fecha entra el usuario
                print (f"Su signo es.") #imprime en pantalla el signo del usuario
            elif (num>=70) and (num<=79):#función para verificar si el número es igual a 10
                print (f"Su signo es.") #imprime en pantalla el signo del usuario
        elif (mes=="JULIO"): #función para verificar a que mes perteneces la información ingresada por el usuario
            if (num>=60) and (num<=69):#función para verificar en que rango de fecha entra el usuario
                print (f"Su signo es.") #imprime en pantalla el signo del usuario
            elif (num>=70) and (num<=79):#función para verificar si el número es igual a 10
                print (f"Su signo es.") #imprime en pantalla el signo del usuario
        elif (mes=="AGOSTO"): #función para verificar si el número es mayor a 10
            if (num>=60) and (num<=69):#función para verificar en que rango de fecha entra el usuario
                print (f"Su signo es.") #imprime en pantalla el signo del usuario
            elif (num>=70) and (num<=79):#función para verificar si el número es igual a 10
                print (f"Su signo es.") #imprime en pantalla el signo del usuario
        elif (mes=="SEPTIEMBRE"): #función para verificar a que mes perteneces la información ingresada por el usuario
            if (num>=60) and (num<=69):#función para verificar en que rango de fecha entra el usuario
                print (f"Su signo es.") #imprime en pantalla el signo del usuario
            elif (num>=70) and (num<=79):#función para verificar si el número es igual a 10
                print (f"Su signo es.") #imprime en pantalla el signo del usuario
        elif (mes=="OCTUBRE"): #función para verificar si el número es mayor a 10
            if (num>=60) and (num<=69):#función para verificar en que rango de fecha entra el usuario
                print (f"Su signo es.") #imprime en pantalla el signo del usuario
            elif (num>=70) and (num<=79):#función para verificar si el número es igual a 10
                print (f"Su signo es.") #imprime en pantalla el signo del usuario
        elif (mes=="NOVIEMBRE"): #función para verificar a que mes perteneces la información ingresada por el usuario
            if (num>=60) and (num<=69):#función para verificar en que rango de fecha entra el usuario
                print (f"Su signo es.") #imprime en pantalla el signo del usuario
            elif (num>=70) and (num<=79):#función para verificar si el número es igual a 10
                print (f"Su signo es.") #imprime en pantalla el signo del usuario
        elif (mes=="DICIEMBRE"): #función para verificar si el número es mayor a 10
            if (num>=60) and (num<=69):#función para verificar en que rango de fecha entra el usuario
                print (f"Su signo es.") #imprime en pantalla el signo del usuario
            elif (num>=70) and (num<=79):#función para verificar si el número es igual a 10
                print (f"Su signo es.") #imprime en pantalla el signo del usuario

        
        otronum = input("¿Desea ingresar otra fecha? (S/N): ").upper() #función que permite al usuario decidir si quiere seguir ejecutando el programa
        if otronum != 'S':
            break 

zodiaco() 