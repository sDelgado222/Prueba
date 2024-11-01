import random


nombre=input("Ingrese su nombre: ")
apellidos=input("Ingrese sus apellidos: ")
edad=int(input("Ingrese su edad: "))
numero_aleatorio=random.randint(1,10)
numero=int(input("Por favor ingrese un número del 1 al 10: "))
if numero==numero_aleatorio:
    print("Felicidades",nombre, apellidos, ", haz ganado!")
else:
    print("No has ganado, pero gracias por participar. El numero correcto era: ", numero_aleatorio)