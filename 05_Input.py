# Entrada de usuario en Python
# La función input() se utiliza para obtener entrada del usuario desde la consola.
# El valor ingresado por el usuario se devuelve como una cadena de texto (str).

# Ejemplo de uso de input()
nombre = input("¿Cuál es tu nombre? ")  # Solicita al usuario que ingrese su nombre
print("Hola, " + nombre + "!")  # Saluda al usuario utilizando el nombre 

# Si queremos obtener un número del usuario, debemos convertir la cadena a un tipo numérico
edad_str = input("¿Cuántos años tienes? ")  # Solicita al usuario que ingrese su edad como cadena
edad = int(edad_str)  # Convierte la cadena a un entero
print("Tienes " + str(edad) + " años.")  # Imprime la edad del usuario

# También podemos hacer la conversión directamente en la función input()
altura = float(input("¿Cuál es tu altura en metros? "))  # Solicita al usuario que ingrese su altura y la convierte a float
print("Tu altura es " + str(altura) + " metros.")  # Imprime la altura del usuario
# print("Tu altura es " + altura + " metros.")  # Esto generará un error porque no se puede concatenar una cadena con un número sin convertir el número a cadena