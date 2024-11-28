#Calcula el factorial de un número ingresado por el usuario 

def factorial():
    while True: #sentencia repetitiva que nos permitirá repetir el programa hasta que las condiciones se cumplan
        print("Calcularemos el factorial de un número.")
        n= int(input("Ingrese un número: " ) )+1
        factor=1
        for i in range(1,n):
            factor=factor*i
        print(f"El factorial de {n-1} es {factor}")

        otronum = input("¿Desea ingresar otro número? (S/N): ").upper() #función que permite al usuario decidir si quiere seguir ejecutando el programa
        if otronum != 'S':
           break 

factorial() #