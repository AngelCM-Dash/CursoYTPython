# Casteo de tipos de datos
# El casteo es el proceso de convertir un valor de un tipo de dato a otro. En Python, existen dos tipos de casteo: implícito y explícito.


# Casteo implícito
a = 5  # int
b = 2.5  # float
c = a + b  # El resultado es un float debido al casteo implícito
print(c)  # 7.5
print(type(c))  # <class 'float'>
print("-"*50)

# Casteo explícito
x = 10  # int
y = float(x)  # Casteo explícito a float
print(y)  # 10.0
print(type(y))  # <class 'float'>
print("-"*50)

# Casteo explícito a int
z = 3.14  # float
w = int(z)  # Casteo explícito a int, se trunca la parte decimal
print(w)  # 3
print(type(w))  # <class 'int'>
print("-"*50)

# Casteo explícito a str
numero = 42
texto = str(numero)  # Casteo explícito a str
print(texto)  # '42'
print(type(texto))  # <class 'str'>
print("-"*50)

#
# numero_str = "3.14"
# numero_int = 45
# print(numero_str + numero_int)
# Esto generará un error porque no se pueden concatenar una cadena y un entero sin convertir el entero a cadena
# Para solucionarlo, podemos convertir el entero a cadena o la cadena a número
print("-"*50)

print(bool(0))  # False, el número 0 se considera falso
print(bool(1))  # True, cualquier número distinto de 0 se considera verdadero
print(bool(""))  # False, una cadena vacía se considera falsa
print(bool("Hola"))  # True, una cadena no vacía se considera verdadera
print(bool([]))  # False, una lista vacía se considera falsa
print(bool([1, 2, 3]))  # True, una lista no vacía se considera verdadera
print(bool(None))  # False, None se considera falso
print("-"*50)


# Redondeo de números flotantes
numero_flotante = 3.14159
numero_flotante2 = round(numero_flotante)  # Redondea al entero más cercano
numero_redondeado = round(numero_flotante, 2)  # Redondea a 2 decimales
numero_redondeado2 = round(3.5)  # Redondea a 3 decimales
print(numero_redondeado)  # 3.14
print(numero_flotante2)  # 3
print(numero_redondeado2)  # 4 , Python redondea al número par más cercano en caso de empate (3.5 se redondea a 4, 2.5 se redondea a 2)


