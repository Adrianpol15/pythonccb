#Area de un terreno
pre=1 
def area (x,y):
    x=float(input("Cual es la anchura de la figura?: "))
    y=float(input("Cual es el alto de la figura?: "))
    res=x*y
    print("Su area es de: ", res)


  
while pre == 1:
   area(1,2)
   
   pre=int(input("Desea continuar? Si. 1, No. 2 "))
   if pre == 2:
      break
   elif pre == 1: 
      pre= 1
   
   else:
    print("Ingrese una opcion correcta ")
    pre=int(input("Quiere continuar? Si. 1, No. 2 "))
