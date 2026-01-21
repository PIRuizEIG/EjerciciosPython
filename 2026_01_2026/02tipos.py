# Números enteros

edad = int(input("Introduce tu edad: "))
print("El tipo de dato es", type(edad))
print("Tu edad es:", edad)

# Decimales
precio = float(input("Introduce el precio del producto:"))
print("El precio es:", precio, "€")
print("El tipo de dato es", type(precio))

# Booleanos

if edad >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")

my_bool = True
my_bool = False
print(type(my_bool))
print(my_bool)

# Cadenas de texto
nombre = "Ana"
apellido = "García"
nombre_completo = nombre + " " + apellido
print(nombre_completo)