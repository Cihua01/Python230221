import math
#declarar las variables ENTRADAS
print ("escribe el valor de pi: ")
pi= float (input ())


radio= float (input ("escribe el valor del radio: "))


#operaciones PROCESO
#area=pi* pow(radio,2)
area=math.pi* pow(radio,2)


perimetro= 2*pi*radio
#area=pi*radio**2

#SALIDA RESULTADO
print(f"el area={area} ")
print (f"el perimetro= {perimetro}")
