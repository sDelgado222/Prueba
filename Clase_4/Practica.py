num=int(input("Digite un número: "))
if num>100:
    numprint=num-100
elif num<=100:
    numprint=num
elif num<0:
    print("Error, por favor intentelo de nuevo")
else:
    print("Error, por favor intentelo de nuevo")
print("El numero ingresado es: ", numprint)