#Solicita un número al usuario y muestra su tabla de multiplicar del 1 al 10.

def multiplicacion ():

    while True: #sentencia repetitiva que nos permitirá repetir el programa hasta que las condiciones se cumplan

        print ("Tablas de multiplicar")

        num= int(input("Ingrese el número del que desee tabla de multiplicar: " )) #imprime en pantalla la solicitud al usuario y le permite ingresar el número
    
        for i in range(1,13): #sentencia repetitiva para que se realice la operación

            print(num,' x ', i ,' =', i*num) 
        
        otronum = input("¿Desea ingresar otro número? (S/N): ").upper() #función que permite al usuario decidir si quiere seguir ejecutando el programa
        if otronum != 'S':
            break
            
multiplicacion()
