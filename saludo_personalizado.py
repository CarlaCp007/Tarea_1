#Crea una función que reciba un nombre como parámetro y retorne un saludo

def saludo(): #se apertura función a utilizar
    
    while True: #sentencia repetitiva que nos permitirá repetir el programa hasta que las condiciones se cumplan
        nombre=str(input("Ingrese su nombre: ")) #función que permite ingresar el nombre al usuario
        print (f"Hola {nombre}.") #Se imprime la función solicitada
        otronum = input("¿Desea ingresar otra vez? (S/N): ").upper() #función que permite al usuario decidir si quiere seguir ejecutando el programa
        if otronum != 'S': #función que da paso a cerrar el programa en caso de que el usuario haya ingresado otra letra
            break #sentencia que cierra la sentencia while

saludo() #sentencia que llama a la función para que está se compile en el programa
