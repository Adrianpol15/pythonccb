# Laboratorio dos
pre = 1
print("Hola, Ordene, esta es la lista de ingredientes: ")
ingredientes=["Torta de carne", "Torta de carne extra", "Tocino", "Lechuga", "Tomate", "Cebolla","Mostaza", "Mayonesa", "Ketchup" ]
print(ingredientes)
#Hice la lista solo para que vieran todos los ingredientes qeu ofrecen

while pre == 1:
   
   
    pre=int(input("Desea Torta de carne? Si. 1, No. 2 "))
    if pre == 2:
      print("Su orden a finalizado ")
      break
      #Ocupe el braek ya que si la orden finaliza el ciclo tambien
    elif pre == 1: 
      pre = 1
   
    else:
      print("Ingrese una opcion correcta como Si. 1 o No. 2 ")
      break
    pre=int(input("Quiere torta de carne extra? Si. 1, No. 2 "))
    if pre == 2:
      print("Su orden a finalizado ")
      break

    else:
      pre=int(input("Desea Tocino? Si. 1, No. 2 "))
    if pre == 2:
      print("Su orden a finalizado ")
      break
    elif pre == 1: 
      pre = 1
   
    else:
      print("Ingrese una opcion correcta como Si. 1 o No. 2 ")
      break
    pre=int(input("Quiere Lechuga? Si. 1, No. 2 "))
    if pre == 2:
      print("Su orden a finalizado ")
      break
    else:
      pre=int(input("Desea Tomate? Si. 1, No. 2 "))
    if pre == 2:
      print("Su orden a finalizado ")
      break
    elif pre == 1: 
      pre = 1
   
    else:
      print("Ingrese una opcion correcta como Si. 1 o No. 2 ")
      break
    pre=int(input("Quiere Cebolla? Si. 1, No. 2 "))
    if pre == 2:
      print("Su orden a finalizado ")
      break

    else:
      pre=int(input("Desea Mostaza? Si. 1, No. 2 "))
    if pre == 2:
      print("Su orden a finalizado ")
      break
    elif pre == 1: 
      pre = 1
   
    else:
      print("Ingrese una opcion correcta como Si. 1 o No. 2 ")
      break
    pre=int(input("Quiere Mayonesa? Si. 1, No. 2 "))
    if pre == 2:
      print("Su orden a finalizado ")
      break
    else:
      
      pre=int(input("Quiere Ketchup? Si. 1, No. 2 "))
    if pre == 1:
      
      print("Su orden a finalizado ")
      break
#En todas ocupe el pre ==1 si pinen Si. 1 y seguira preguntando el programa hasta qeu pongan No. 2 y cuando eso pase finalizara el ciclo y aparecera le mensaje Su orden fue finalizada.
