#Ingrese objetos.
n1 = str(input("Ingrese objetos: "))
n2 = "Fin"
estalista=[]
while n2 != n1:
  n1=str(input("Ingrese otro objeto e ingrese la palabra 'Fin' para finalizar: "))
  estalista.append(n1)
  
print(estalista)
