#Solicita el día y mes de nacimiento y determina el signo zodiacal del usuario.

def zodiaco():
    while True: #sentencia repetitiva que nos permitirá repetir el programa hasta que las condiciones se cumplan

        print ("Verificaremos cual es su signo zodiacal.") #se imprime en pantalla instrucciones para el usuario
        num= int(input("Ingrese su día de nacimiento: " ) )#imprime en pantalla la solicitud al usuario y le permite ingresar el número, el mismo que es declarado como una variable entera
        mes= str(input("Ingrese su mes de nacimiento: " ) ).upper()#imprime en pantalla la solicitud al usuario y le permite ingresar el número, el mismo que es declarado como una variable entera    
        if (mes=="ENERO"): #función para verificar a que mes perteneces la información ingresada por el usuario
            if (num>=1) and (num<=19):#función para verificar en que rango de fecha entra el usuario
                print (f"Su signo es Capricornio.") #imprime en pantalla el signo del usuario
            elif (num>=20) and (num<=31):#función para verificar si el número es igual a 10
                print (f"Su signo es Acuario.") #imprime en pantalla el signo del usuario
        elif (mes=="FEBRERO"): #función para verificar si el número es mayor a 10
            if (num>=1) and (num<=18):#función para verificar en que rango de fecha entra el usuario
                print (f"Su signo es Acuario.") #imprime en pantalla el signo del usuario
            elif (num>=19) and (num<=29):#función para verificar si el número es igual a 10
                print (f"Su signo es Piscis.") #imprime en pantalla el signo del usuario
        elif (mes=="MARZO"): #función para verificar a que mes perteneces la información ingresada por el usuario
            if (num>=1) and (num<=20):#función para verificar en que rango de fecha entra el usuario
                print (f"Su signo es Piscis.") #imprime en pantalla el signo del usuario
            elif (num>=21) and (num<=31):#función para verificar si el número es igual a 10
                print (f"Su signo es Aries.") #imprime en pantalla el signo del usuario
        elif (mes=="ABRIL"): #función para verificar si el número es mayor a 10
            if (num>=1) and (num<=19):#función para verificar en que rango de fecha entra el usuario
                print (f"Su signo es Aries.") #imprime en pantalla el signo del usuario
            elif (num>=20) and (num<=30):#función para verificar si el número es igual a 10
                print (f"Su signo es Tauro.") #imprime en pantalla el signo del usuario
        elif (mes=="MAYO"): #función para verificar a que mes perteneces la información ingresada por el usuario
            if (num>=1) and (num<=20):#función para verificar en que rango de fecha entra el usuario
                print (f"Su signo es Tauro.") #imprime en pantalla el signo del usuario
            elif (num>=21) and (num<=31):#función para verificar si el número es igual a 10
                print (f"Su signo es Géminis.") #imprime en pantalla el signo del usuario
        elif (mes=="JUNIO"): #función para verificar si el número es mayor a 10
            if (num>=1) and (num<=20):#función para verificar en que rango de fecha entra el usuario
                print (f"Su signo es Géminis.") #imprime en pantalla el signo del usuario
            elif (num>=21) and (num<=30):#función para verificar si el número es igual a 10
                print (f"Su signo es Cancer.") #imprime en pantalla el signo del usuario
        elif (mes=="JULIO") and (num>=1) and (num<=22): #función para verificar a que mes perteneces la información ingresada por el usuario
            print (f"Su signo es Cancer.") #imprime en pantalla el signo del usuario
        elif (mes=="JULIO") and (num>=23) and (num<=31): #función para verificar a que mes perteneces la información ingresada por el usuario
            print (f"Su signo es Leo.") #imprime en pantalla el signo del usuario    
        elif (mes=="AGOSTO") and (num<=1) and (num<=22):#función para verificar en que rango de fecha entra el usuario
            print (f"Su signo es Leo.") #imprime en pantalla el signo del usuario
        elif (mes=="AGOSTO") and (num>=23) and (num<=31):#función para verificar en que rango de fecha entra el usuario
            print (f"Su signo es VIRGO.") #imprime en pantalla el signo del usuario
        elif (mes=="SEPTIEMBRE") and (num>=1) and (num<=23):#función para verificar en que rango de fecha entra el usuario
                print (f"Su signo es Libra.") #imprime en pantalla el signo del usuario
        elif (mes=="SEPTIEMBRE") and (num>=22) and (num<=30):#función para verificar en que rango de fecha entra el usuario
                print (f"Su signo es Libra.") #imprime en pantalla el signo del usuario
        elif (mes=="OCTUBRE") and (num>=1) and (num<=22):#función para verificar en que rango de fecha entra el usuario
                print (f"Su signo es Libra.") #imprime en pantalla el signo del usuario
        elif (mes=="OCTUBRE") and (num>=23) and (num<=31):#función para verificar en que rango de fecha entra el usuario
                print (f"Su signo es Escorpio.") #imprime en pantalla el signo del usuario
        elif (mes=="NOVIEMBRE") and (num>=1) and (num<=22): #función para verificar a que mes perteneces la información ingresada por el usuario
            print (f"Su signo es Escorpio.") #imprime en pantalla el signo del usuario
        elif (mes=="NOVIEMBRE") and (num>=23) and (num<=30): #función para verificar a que mes perteneces la información ingresada por el usuario
            print (f"Su signo es Sagitario.") #imprime en pantalla el signo del usuario
        elif (mes=="DICIEMBRE") and (num>=1) and (num<=21): #función para verificar si el número es mayor a 10
            print (f"Su signo es Sagitario.") #imprime en pantalla el signo del usuario
        elif (mes=="DICIEMBRE") and (num>=22) and (num<=31): #función para verificar si el número es mayor a 10    
            print (f"Su signo es Capricornio.") #imprime en pantalla el signo del usuario
        else:
            "Fuera de rango."
        otronum = input("¿Desea ingresar otra fecha? (S/N): ").upper() #función que permite al usuario decidir si quiere seguir ejecutando el programa
        if otronum != 'S':
            break 

zodiaco() 