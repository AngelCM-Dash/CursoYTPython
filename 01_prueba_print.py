# Este es un programa de ejemplo que muestra un mensaje en la consola.
print("Soy guapo")
#print("Soy", "guapo") # Esto imprimirá "Soy guapo" con un espacio entre las palabras.
print("Soy", "inteligente")

# El parámetro 'sep' en la función print() se utiliza para especificar el separador entre los argumentos que se imprimen.
# Por defecto, el separador es un espacio (" "). En este caso, al usar sep="-"
print("Soy", "inteligente", sep="-")

# El parámetro 'end' en la función print() se utiliza para especificar lo que se imprime al final de la línea.
# Por defecto, es un salto de línea ("\n"), lo que significa que cada llamada a print() imprimirá en una nueva línea.
# Al usar end=" ", el siguiente print() continuará en la misma línea.
print("El", "gato", end=" ")
print("está", end=" ")
print("en la casa.")

# Puedes usar print() para imprimir cualquier tipo de dato, como números, listas, diccionarios, etc.
print(45)
print([1, 2, 3, 4, 5])