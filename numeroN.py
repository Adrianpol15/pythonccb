#que pida numero N
n=int(input("Ingrese un numero: ")) #solicitamos un numero

contador=1
divisores=0

while contador<=n:
  residuo=n%contador
  print(residuo)
  #Saca el resuduo y hace la divicion con el contador.
  if residuo == 0:
    divisores=divisores+1
  contador=contador+1
  #Si el residuo es 0 empieza a dividir el numero y el contador.

if divisores==2:
  print ("es primo")
  print("Tiene ",divisores, " divisores")
else:
  print("no es primo")
  print("Tiene ",divisores, " divisores")
