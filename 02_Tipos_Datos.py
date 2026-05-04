# Tipos de datos en python
# Enteros
x = 10
print(type(x))  # <class 'int'>
print(type(654513213546546543123134))  # <class 'int'>, Python maneja enteros de tamaño arbitrario
print(type(-5))  # <class 'int'>, los enteros pueden ser negativos, cero o positivos

# Flotantes
y = 3.14
print(type(y))  # <class 'float'>
print(type(1.0))  # <class 'float'>, los números con punto decimal son flotantes
print(type(-0.001))  # <class 'float'>, los flotantes también pueden ser negativos

# Complejos
z = 2 + 3j
print(type(z))  # <class 'complex'>

# Cadenas de texto
nombre = "Juan"
nombre2 = 'María'
print(type(nombre))  # <class 'str'>
print(type('Hola, mundo!'))  # <class 'str'>, las cadenas pueden usar comillas simples o dobles
print(type("""Esto es una cadena de texto
           con comillas
           triples"""))  # <class 'str'>, las comillas triples permiten cadenas multilínea

# Booleanos
es_estudiante = True
print(type(es_estudiante))  # <class 'bool'> ,los booleanos pueden ser True o False

# None
valor_desconocido = None
print(type(valor_desconocido))  # <class 'NoneType'>, None representa la ausencia de valor

# Listas
numeros = [1, 2, 3, 4, 5]
print(type(numeros))  # <class 'list'>
# Tuplas
coordenadas = (10.0, 20.0)
print(type(coordenadas))  # <class 'tuple'>
