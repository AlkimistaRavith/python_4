
with open("lorem_ipsum.txt", "r") as file:
    texto = file.read()

caracteres_distintos = set(texto)
print(f"El número de caracteres distintos es: {len(caracteres_distintos)}")

palabras = texto.split()
palabras_distintas = set(palabras)
print(f"El número de palabras distintas es: {len(palabras_distintas)}")