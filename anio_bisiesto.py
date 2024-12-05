#Solicita un año y determina si es bisiesto (divisible entre 4 pero no entre 100, excepto si es divisible entre 400).

def bisiesto():
    while True: #sentencia repetitiva que nos permitirá repetir el programa hasta que las condiciones se cumplan
        num= int(input("Ingrese un año: " ) )#imprime en pantalla la solicitud al usuario y le permite ingresar el número, el mismo que es declarado como una variable entera
        print ("Verificaremos si el año es bisiesto.") #se imprime en pantalla instrucciones para el usuario
        resto1=num%400
        resto2=num%100
        resto3=num%4
        if (resto1 == 0): 
            print (f"El año {num} es bisiesto.")
        elif (resto3 == 0) and (resto2!= 0): 
            print (f"El año {num} es bisiesto.")
        else:
            print (f"El año {num} no es bisiesto.")

        otronum = input("¿Desea ingresar otro número? (S/N): ").upper() #función que permite al usuario decidir si quiere seguir ejecutando el programa
        if otronum != 'S':
            break 

bisiesto()

        