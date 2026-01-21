nombre = input("Introduzca su nombre:")
edad = int(input("Introduzca su edad:"))
altura = float(input("Introduzca su altura:"))
mayor = edad >= 18

print("Nombre:", nombre, "Edad:", edad, "Altura:", altura, "Mayor de edad:", mayor)
print("Nombre:", type(nombre), "Edad:", type(edad), "Altura:", type(altura), "Mayor de edad:", type(mayor))