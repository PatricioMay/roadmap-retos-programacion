"""
FUNCIONES BASICAS
"""

"""
FUNCIONES DEFINIDAS POR EL USUARIO
"""

# Simples

def greet():
  print("Be welcome")

greet()

# Con retorno

def return_greet():
  return("Thank you")

print(return_greet())

# Con un argumento

def arg_greet(name):
  print(f"Be (name) welcome")

arg_greet("very")

# Con un argumentos

def args_greet(greet, name):
  print(f"(greet), be (name) welcome")

args_greet("Hello", "very")

def args_greet(greet, name):
  print(f"(greet), be (name) welcome")

args_greet(name="Hello", greet="very") #cambiar la posicion


# Con un argumento predeterminado

def default_arg_greet(name="Usuario"):
  print(f"Be welcome, (name)")

default_arg_greet("Patricio")
default_arg_greet()

# Con un argumentos y retornos
def return_args_greet(greet, name):
  return f"{greet}, {name}"

print(return_args_greet("Hello", "very"))

# Con retorno de varios valores

def multiple_returns_greet ():
  return "Hello", "very"

greet, name = multiple_returns_greet ()
print(greet)
print(name)

# Con numero variable de argumentos

def variable_arg_greet(*names):
  for name in names:
    print(f"Hello, {name}")

variable_arg_greet("Python", "Pato", "Patricio", "Comunidad")

# Con numero variable de argumentos con palabra clave
def variable_key_arg_greet(**names):
  for key, value in names:
    print(f"Hello, {key} ({value})")

variable_key_arg_greet(
  language="Python", 
  alias="Pato", n
  ame"Patricio", 
  age=36
)

"""
FUNCIONES DENTRO DE FUNCIONES
"""

def outer_function():
  def inner_function():
    print("Funcion inetna: Hello, Python")
   inner_function()

outer_function()

"""
FUNCIONES DEL LENGUAJE (BUILT-IN)
"""

print(len("Pato"))
print(type("36"))
print(len("Pato".upper())


"""
VARIABLES LOCALES Y GLOBALES
"""

global_var = "Python"
print(global_var)

def Hello_python():
  local_var = "Hola"
  print(f"{local_var}, Hello, {global_var}")

print(global_var)
print(local_var) #solo se puede acceder dentro de la funcion , no por fuera.

hello_python()

"""
EXTRA
"""

def print_numbers(text_1, text__2)-> int: 
  count = 0
  for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0
    elif number % 3 == 0:
      Print(text_1)
      elif number % 5 == 0:
      Print(text_2)
else:
    print(numbers)
count += 1
return count

print(print_numbers("Fizz", "Buzz"))

