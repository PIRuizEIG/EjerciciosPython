# Variables
a = 10
b = 3

# Operadores

print("Suma ", a, " + ", b, a + b) # 13
print("Resta ", a, " - ", b, (a - b)) # 7
print("Multiplicación ", a, " * ", b, (a * b)) # 30
print("División ", a, " / ", b, (a / b)) # 3.333...
print("División de enteros ", a, " // ", b, (a // b)) # 3
print("Resto de división ", a, " % ", b, (a % b)) # 1
print("Potencia ", a, " ** ", b, (a ** b)) # 1000

# Operadores logicos

edad = 20
tiene_carnet = True
tiene_coche = False

print("Es mayor de edad", edad >= 18)
print("Tiene carnet", tiene_carnet)
print("Es mayor de edad y tiene carnet", edad >= 18 and tiene_carnet)
print("Es menor de edad o tiene carnet", edad < 18 or tiene_carnet)
print("No es mayor de edad", not edad >= 18)
print("Tiene coche", tiene_coche)
print("Tiene coche y tiene carnet", tiene_coche and tiene_carnet)
print("Tiene coche o tiene carnet", tiene_coche or tiene_carnet)
print("No tiene coche", not tiene_coche)

# Operadores de asignación

a += b # a = a + b
a -= b # a = a - b
a *= b # a = a * b
a /= b # a = a / b
a //= b # a = a // b
a %= b # a = a % b
a **= b # a = a ** b
