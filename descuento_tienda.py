#Una tienda ofrece un 20% de descuento si el cliente gasta más de $100. Escribe un programa que calcule el monto final.

def descuento(): #se apertura función a utilizar
    while True: #sentencia repetitiva que nos permitirá repetir el programa hasta que las condiciones se cumplan
        descuento=float
        valor=float(input("Ingrese el valor de su compra.")) #se imprime en pantalla instrucciones para el usuario
        if(valor>100):
            descuento=(valor*0.20)
            final=(valor-descuento)
            print(f"Usted ha obtenido un descuento del 20%. \nSu descuento es de ${descuento}, el total a pagar es de ${final}.")
        else:
            print(f"Su compra es de ${valor}. No ha obtenido descuento.")
        otronum = input("¿Desea ingresar otro valor? (S/N): ").upper() #función que permite al usuario decidir si quiere seguir ejecutando el programa
        if otronum != 'S':
            break 

descuento()