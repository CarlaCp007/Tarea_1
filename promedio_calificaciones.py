#Solicita calificaciones al usuario (hasta que ingrese -1) y calcula el promedio.

def promedio(): #se apertura función a utilizar
    
    while True: #sentencia repetitiva que nos permitirá repetir el programa hasta que las condiciones se cumplan

        calificacion=0.0
        suma=0.0
        promedio=0.0
        contador=-1
        print("Calcularemos su nota final")
        while(calificacion!=(-1)):
            calificacion= float(input("Ingrese calificación: " ) )#imprime en pantalla la solicitud al usuario y le permite ingresar el número, el mismo que es declarado como una variable entera  
            suma=suma+calificacion
            contador=contador+1
        else:
            suma=suma+1
            promedio=suma/contador
            print(f"Su promedio es de: {promedio}")
        
        otronum = input("¿Desea ingresar otra vez? (S/N): ").upper() #función que permite al usuario decidir si quiere seguir ejecutando el programa
        if otronum != 'S':
           break 

promedio() 