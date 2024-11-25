#Solicita una edad y clasifica al usuario como niño (0-12), adolescente (13-17) o adulto (18+).

def edad(): #se apertura función a utilizar
    
    while True: #sentencia repetitiva que nos permitirá repetir el programa hasta que las condiciones se cumplan

        num1= int(input ("Ingrese su edad: ")) #se imprime en pantalla instrucciones para el usuario
        print ("Lo clasificaremos por su edad.") #se imprime en pantalla instrucciones para el usuario
        if (num1 <= 12): #función para verificar si el número es mayor a 10
            print (f"Eres un niño.")
        elif (num1>=13) and (num1<=17):#función para verificar si el número es igual a 10
            print (f"Eres un adolescente.")
        else:
            print (f"Eres un adulto.")
        otronum = input("¿Desea ingresar otra edad? (S/N): ").upper() #función que permite al usuario decidir si quiere seguir ejecutando el programa
        if otronum != 'S':
            break 

edad()