#	Solicita un número al usuario y determina si es par o impar.

def par_impar(): #se apertura función a utilizar
    
    while True: #sentencia repetitiva que nos permitirá repetir el programa hasta que las condiciones se cumplan

        num= int(input("Ingrese un número: \n" ) )#imprime en pantalla la solicitud al usuario y le permite ingresar el número, el mismo que es declarado como una variable entera
        print ("Verificaremos si el número es par o impar.") #se imprime en pantalla instrucciones para el usuario
        resto=num%2
        if (resto == 0): #función para verificar si el número es mayor a 10
            print (f"El número {num} es par")
        else:#función para verificar si el número es igual a 10
            print (f"El número {num} es impar")
        otronum = input("¿Desea ingresar otro número? (S/N): ").upper() #función que permite al usuario decidir si quiere seguir ejecutando el programa
        if otronum != 'S':
            break 

par_impar() 