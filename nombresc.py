Detecta si los nombres tienen alguna concidencia.
print("Ingrese los nombres con minusculas")
a=str(input("Ingrese el primer nombre: "))
b=str(input("Ingrese el segundo nombre: "))
if a[-1] == b[-1] or a[0] == b[0]:
  print("Hay concidencia ")
else:
  print("No hay concidencia ") 
