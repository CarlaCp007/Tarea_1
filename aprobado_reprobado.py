#Solicita la calificación de un estudiante y determina si está aprobado (mayor o igual a 7) o reprobado.

def notas(): #se apertura función a utilizar

    while True: #sentencia repetitiva que nos permitirá repetir el programa hasta que las condiciones se cumplan

         print ("Verificaremos si el estudiante aprueba o reprueba el semestre.") #se imprime en pantalla instrucciones para el usuario
         num= float(input("Ingrese la nota final: " ) )#imprime en pantalla la solicitud al usuario y le permite ingresar el número, el mismo que es declarado como una variable entera
         if (num >= 7): #función para verificar si el número es mayor a 10
            print (f"El estudiante ha aprobado")

         else:#en el caso de ser negativas las dos sentencias anteriores se descarta como menor
            print ("El estudiante ha reprobado")

         otronum = input("¿Desea ingresar otro número? (S/N): ").upper() #función que permite al usuario decidir si quiere seguir ejecutando el programa
         if otronum != 'S':
            break

notas() 
