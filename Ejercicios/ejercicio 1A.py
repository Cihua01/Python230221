#declarar las variables ENTRADAS
print ("escribe calificacion1: ")
calificacion1= float (input ())

calificacion2= float (input ("escribe calificacion2: "))

print ("escribe calificacion3: ")
calificacion3= float (input ())


#operaciones PROCESO
suma=calificacion1 + calificacion2 + calificacion3
promedio=(suma/3)

if (promedio<=5.99):
    print(f"Reprobado={promedio} ")
elif (promedio>=6):
    print(f"Aprobado={promedio} ")
else:
    print(f"Otro caso={promedio} ")
