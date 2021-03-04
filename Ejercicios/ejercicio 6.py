import math
#declarar las variables ENTRADAS
print ("escribe el valor de a:")
a= float (input ())
print ("escribe el valor de b:")
b= float (input ())
print ("escribe el valor de c:")
c= float (input ())

#operaciones PROCESO

formula_generalx1=(-b+(pow(b**2-4*a*c,1/2)))/(2*a)
formula_generalx2=(-b-(pow(b**2-4*a*c,1/2)))/(2*a)

#SALIDA RESULTADO
print(f"formula general={formula_generalx1} ")
print(f"formula general={formula_generalx2} ")