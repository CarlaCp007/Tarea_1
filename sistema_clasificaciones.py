#Solicita una calificación numérica y devuelve la letra correspondiente:

def clasificaciones():
    while True: #sentencia repetitiva que nos permitirá repetir el programa hasta que las condiciones se cumplan

            print ("Verificaremos cual es su calificación según su puntaje.") #se imprime en pantalla instrucciones para el usuario
            num= int(input("Ingrese su calificación: \n" ) )#imprime en pantalla la solicitud al usuario y le permite ingresar el número, el mismo que es declarado como una variable entera
            if (num < 60): #función para verificar si el número es mayor a 10
                print (f"Su calificación es F.")
            elif (num>=60) and (num<=69):#función para verificar si el número es igual a 10
                print (f"Su calificación es D.")
            elif (num>=70) and (num<=79):#función para verificar si el número es igual a 10
                print (f"Su calificación es C")
            elif (num>=80) and (num<=89):#función para verificar si el número es igual a 10
                print (f"Su calificación es B.")
            elif (num>=90) and (num<=100):#función para verificar si el número es igual a 10
                print (f"Su calificación es A")
            else: #en el caso de ser negativas las dos sentencias anteriores se descarta como menor
                print (f"Fuera de rango.")
            otronum = input("¿Desea ingresar otra calificación? (S/N): ").upper() #función que permite al usuario decidir si quiere seguir ejecutando el programa
            if otronum != 'S':
                break 

clasificaciones() 