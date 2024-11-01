print("Bienvenido a la sala de videojuegos!!Le vamos a informar el valor de su entrada, por favor ingrese la informacion que se le solicite.")
edad = int(input( "Ingrese su edad: "))
if edad<10: 
    print("Costo: 3000")
elif edad<15: 
    print("Costo: 5000")
elif edad<18: 
    print("Costo: 7500")
else:
    print("Costo: 10000")