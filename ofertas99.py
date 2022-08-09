#Hace ofertas de un producto.
print("OFERTAS LA TORRE")
p1=str(input("INGRESE PRODUCTO: "))
pr=float(input("INGRESE PRECIO: "))
c=int(input ("INGRESE CANTIDAD DEL PRODUCTO: "))
d=0.25
if c>=5:
  print("EL PRECIO REGULAR ES DE: ")
  print(pr) 
  pd=pr*d
  print("USTED AHORRO: ")
  print(pd)
  dt=pr-pd
  print("EL PRECIO CON EL DESCUENTO ES: ")
  print(dt)
else:
  ("NO APLICA EL DESCUENTO, EL PRECIO ES: ")
  print(pr)
