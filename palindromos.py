#Ve si las palabras son palindromos. 
n1=str(input("Ingresar la palabra: "))
n4=n1.lower()
n2=''.join(reversed(n1))
n3=n2.lower()
n5= n4.replace(" ", "")
n6= n3.replace(" ", "")
if n5 == n6:
 print("La palabra que ingreso si es un palindromo")
else:
  print("No es un polindromo")
