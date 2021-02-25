print("Escribe número 1: ")
numero1 = int(input())
print("Escribe número 2: ")
numero2 = int(input())

suma = numero1 + numero2
resta = numero1 - numero2

potencia1 = pow(numero1, numero2)
potencia2 = numero1 ** numero2

raiz_cuadrada = pow(numero1, 1/2)
raiz_cubica = pow(numero1, 1/3)

modulo = numero1 % numero2

# print("La suma es igual a " + str(suma))
print(f"La suma = {suma}")
print(f"La potencia1 = {potencia1}")
print(f"La potencia2 = {potencia2}")
print(f"La raíz cuadrada = {raiz_cuadrada}")
print(f"La raíz cúbica = {raiz_cubica}")
print(f"El módulo o residuo = {modulo}")