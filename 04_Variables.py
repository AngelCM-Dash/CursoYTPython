# Las variables en python son contenedores que almacenan datos.
# No es necesario declarar el tipo de variable, ya que Python lo infiere automáticamente.
# Para asignar un valor a una variable, se utiliza el operador de asignación (=).

# Ejemplo de variables
nombre = "Alice"  # Variable de tipo str
edad = 30  # Variable de tipo int
altura = 1.75  # Variable de tipo float
print(nombre)  # Alice
print(edad)  # 30
print(altura)  # 1.75
print(type(altura))  # la variables altura es de tipo float
print("-"*50)

# Es posible cambiar el valor de una variable en cualquier momento
nombre = "Bob"  # Ahora la variable nombre tiene el valor "Bob"
altura = "alto"  # Ahora la variable altura tiene el valor "alto", aunque antes era un número
print(nombre)  # Bob
print(altura)  # alto ,
print(type(altura))  # la variable altura ahora es de tipo str
print("-"*50)

# Nombre de variables
# Las variables deben seguir ciertas reglas para ser válidas:
# 1. Deben comenzar con una letra (a-z, A-Z) o un guion bajo (_).
# 2. El resto del nombre puede contener letras, números o guiones bajos.
# 3. No pueden ser palabras reservadas de Python (como if, for, while, etc.).
# 4. Se recomienda usar nombres descriptivos para facilitar la lectura del código.
# Ejemplos de nombres de variables válidos
nombre_usuario = "Alice"
edad_usuario = 30
altura_usuario = 1.75
print(nombre_usuario)  # Alice

# Ejemplos de nombres de variables no válidos
# 1nombre = "Bob"  # No puede comenzar con un número
# @nombre = "Charlie"  # No puede contener caracteres especiales como @
# mi variable = "David"  # No puede contener espacios
# mi-variable = "Eve"  # No puede contener guiones
# for = "David"  # No puede ser una palabra reservada

# Convenciones de nombres
# En Python, se siguen ciertas convenciones de nombres para mejorar la legibilidad del código:
# 1. snake_case: Se utiliza para nombrar variables y funciones, donde las palabras se separan por guiones bajos. Ejemplo: nombre_usuario, calcular_area().
# 2. CamelCase: Se utiliza para nombrar clases, donde cada palabra comienza con mayúscula. Ejemplo: MiClase, Persona.
# 3. UPPER_SNAKE_CASE: Se utiliza para nombrar constantes, donde las palabras se separan por guiones bajos y
# todas las letras son mayúsculas. Ejemplo: PI = 3.14159, MAX_VALUE = 100.
PI = 3.14159  # Constante, se recomienda usar mayúsculas para indicar que no debe cambiar su valor
print(PI)  # 3.14159
PORCENTAJEIGV = 0.18  # Constante para el porcentaje del IGV en Perú
print(PORCENTAJEIGV)  # 0.18
