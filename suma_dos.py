#Escribe una función que reciba dos números como parámetros y retorne su suma.

def suma(): #se apertura función a utilizar
    
    while True: #sentencia repetitiva que nos permitirá repetir el programa hasta que las condiciones se cumplan

        
        print("Suma de dos números.")
        num1= int(input("Ingrese primer número: " ) )#imprime en pantalla la solicitud al usuario y le permite ingresar el número, el mismo que es declarado como una variable entera  
        num2= int(input("Ingrese segundo número: " ) )#imprime en pantalla la solicitud al usuario y le permite ingresar el número, el mismo que es declarado como una variable entera  
        suma=num1+num2
        print(f"{num1}+{num2}={suma}")
        
        otronum = input("¿Desea hacerlo otra vez? (S/N): ").upper() #función que permite al usuario decidir si quiere seguir ejecutando el programa
        if otronum != 'S':
           break 

suma() 
