from math import pi

def volumen(r,h):
  V = pi * r**2 *h 
  return V
#todo va a aestar en V empezara con pi luego se multiplicara con r y h que es radi y altura y nos devolvera V.
radio = float(input("Radrio: "))
altura = float(input("Altura: "))
vol = volumen(radio, altura)
print("Res", vol)
#pedira los valores de r y h, luego hara el volumen que es radio por altura y va a imprimir el resultado qeu seria el volumen
