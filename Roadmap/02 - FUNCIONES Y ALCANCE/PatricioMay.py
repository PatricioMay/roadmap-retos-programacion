"""
operadores
"""

# operadores aritmeticos
print(f"suma: 2 + 2 = {2 + 2}")
print(f"resta: 2 - 2 = {2 - 2}")
print(f"multiplicacion: 2 * 2 = {2 * 2}")
print(f"division: 2 / 2 = {2 / 2}")
print(f"modulo: 2 % 2 = {2 % 2}")
print(f"multiplicacion entera: 2 ** 2 = {2 * 2}")
print(f"division entera: 2 // 2 = {2 // 2}")

# operadores de comparacion
print(f"igualdad: 2 == 4 es {10 == 3}")
print(f"desigualdad: 2 != 4 es {10 != 3}")
print(f"mayor que: 2 > 4 es {10 > 3}")
print(f"menor que: 2< 4 es {10 < 3}")
print(f"mayor o igual que: 2 >= 4 es {10 >= 3}")
print(f"menor o igual que: 2 <= 4 es {10 <= 3}")

# operadores logicos
print(f"and: 2 + 2 == 4 and 8 - 1 == 7 es { 2 + 2 == 4 and 8 - 1 == 7}")
print(f"or: 2 + 2 == 4 or 8 - 1 == 7 es { 2 + 2 == 5 or 8 - 1 == 7}")
print(f"not: not 5 + 3 == 7 es {not 5 + 3 == 7}")

#operadores de asignacion
My_number = 12 #asignacion
print(My_number)
My_number += 1 #suma y asignacion
print(My_number)
My_number -= 1 #resta y asignacion
print(My_number)
My_number *= 1 #multiplicacion y asignacion
print(My_number)
My_number /= 1 #division y asignacion
print(My_number)
My_number %= 2 #modulo y asignacion
print(My_number)
My_number **= 1 #exponente y asignacion
print(My_number)
My_number //= 1 #division entera y asignacion

#operadores de identidad
my_new_number = 1.0
print(f"My_number is my_new_number es {My_number is my_new_number}")
my_new_number = 1.0
print(f"My_number is not my_new_number no es {My_number is not my_new_number}")

my_new_number = My_number
print(f"My_number is my_new_number es {My_number is my_new_number}")

#operadores de pertenencia
print(f"'a' in 'car' = {'a' in 'car'}")
print(f"'o' not in 'car' = {'a' not in 'car'}")

#operadores de bit
x = 5 # 101
z = 2 # 10

print(f"and: {5 & 2}")
print(f"or: {5 | 2}")
print(f"xor: {5 ^ 2}")
print(f"not: {~2}")
print(f"desplazamiento a la derecha: 5 >> 2 = {5 >> 2}")
print(f"desplazamiento a la izquierda: 5 << 2 = {5 << 2}")

"""
estructuras de control
"""

#condicionales

my_string = "Pato"

if my_string == "Pato" :
  print("my_string es 'Pato'")

else:
  print("my_string no es 'Pato'")

if my_string == "Pato" :
  print("my_string es 'Pato'")
elif my_string == "Patito"
else:
  print("my_string no es 'Pato' ni 'Patito'")

#interactivas
for i in range (12):
  print(i)
  
i = 0

while i <= 0:
  print(i)

  while i <= 10:
  print(i)
  i += 1

#manejo de excepciones
try:
  print(10 / 0)
except:
  print("se ha producido un error")
finally:
  print("ha finalizado el manejo de excepciones")

"""
extra
"""

for number in range (10, 56):
  if number % 2 == 0 and number != 16  and number % 3 != 0:
  print(number)









