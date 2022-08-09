#Mayor menor
n1=float(input("Ingrese un numero: "))
n2=float(input("Ingrese otro numero: "))
n3=float(input("Ingrese otro numero: "))
if n1>n2 and n1>n3:
  mayor=n1
  if n2>n3:
  
    print(mayor)
    print(n2)
    print(n3)
  else:
    medio=n3
    menor=n2
elif n2>n1 and n2>n3:
  mayor=n2
  if n3>n1:
    
    print(mayor)
    print(n3)
    print(n1)
  else:
    medio=n1
    menor=n3
elif n3>n1 and n3>n2:
  mayor=n3
  if n2>n1:
    
    
    print(mayor)
    print(n2)
    print(n1)
  else:
    medio=n2
    menor=n1
