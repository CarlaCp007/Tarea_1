#Solicita dos números y una operación (+, -, *, /) y realiza el cálculo correspondiente.

print("Calculadora")
num1=0
num2=0
resul=0

def calculadora():
    while True:
        print(""" Elija la operación que desea realizar
              1) Suma
              2) Resta
              3) Multiplicación
              4) División 
              """)
        
        opcion=int(input("Seleccione una opción: "))
        while opcion>=5:
            print ("Fuera de rango")
            opcion=int(input("Seleccione una opción: "))
        else:
            print("Ingrese los números que desea usar:")   
        num1=int(input("Primer número: "))
        num2=int(input("Segundo número: "))
        if opcion==1:
            resul=num1+num2
            print(f"{num1}+{num2}={resul}")
        elif opcion==2:
            resul=num1-num2
            print(f"{num1}-{num2}={resul}")
        elif opcion==3:
            resul=num1*num2
            print(f"{num1}*{num2}={resul}")
        elif opcion==4:
            resul=num1/num2
            print(f"{num1}/{num2}={resul}")
        else:
            print ("Fuera de rango")
        
        seguir = input("¿Desea seguir usando la calculadora? (S/N): ").upper()
        if seguir != 'S':
            break
    else:
        print("Es un gusto haberte ayudado.\n \f ¡Adiós!")

calculadora()
