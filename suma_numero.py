#Calcula y muestra la suma de los números del 1 al 10.

def suma(): #se apertura función a utilizar
    suma=0 #se declara el valor inicial de la variable suma en la que se almacenera la suma de los números
    for i in range(1,11): #sentencia repetitiva para que se realice la operación
        suma=(suma+i) #función que realiza la suma de los digitos
    print(suma) #imprime en pantalla el resultado final

suma() #