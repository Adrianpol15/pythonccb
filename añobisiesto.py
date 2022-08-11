#Programa para saber si al año es bisiesto.
a = int(input("Ingrese el año para saber si es bisiestro: "))
if a % 4 == 0:
    if a % 100 == 0:
        if a % 400 == 0:
            print("El año es bisiesto")
        else:
            print("El año no es bisiesto")
    else:
        print("El año es bisiesto")
else:
    print("El año no es bisiesto")
