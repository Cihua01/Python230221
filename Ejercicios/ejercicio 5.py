import math
#declarar las variables ENTRADAS
print ("escribe los grados centigrados:")
grados_centigrados= float (input ())
print ("escribe los grados fahrenheit:")
grados_fahrenheit= float (input ())
print ("escribe los grados kelvin:")
grados_kelvin= float (input ())



#operaciones PROCESO
#edad de la persona=año actual- año de nacimiento
grados_fahrenheit_resultado1= (grados_centigrados * 9/5) + 32

grados_kelvin_resultado1=grados_centigrados + 273.15

grados_centigrados_resultado1=(32* grados_fahrenheit - 32) * 5/9

grados_kelvin_resultado2=(32 * grados_fahrenheit - 32) * 5/9 + 273.15

grados_fahrenheit_resultado2=(grados_kelvin - 273.15)* 9/5 + 32 

grados_centigrados_resultado2=grados_kelvin - 273.15



#SALIDA RESULTADO
print(f"grados centigrados={grados_fahrenheit_resultado1} ")
print(f"grados centigrados={grados_kelvin_resultado1}")
print(f"grados fahrenheit={grados_centigrados_resultado1}")
print(f"grados fahrenheit={grados_kelvin_resultado2}")
print(f"grados_kelvin={grados_fahrenheit_resultado2}")
print(f"grados_kelvin={grados_centigrados_resultado2}")

