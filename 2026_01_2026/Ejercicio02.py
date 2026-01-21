import math

# Pedir los catetos
c1 = float(input("Introduce distancia al punto 1: "))
c2 = float(input("Introduce distancia al punto 2: "))
# Calcular la hipotenusa
h = math.sqrt(c1**2 + c2**2)
# Mostrar el resultado
print("La hipotenusa es: ", h)