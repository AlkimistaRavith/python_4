
with open("lorem_ipsum.txt", "r") as file:
    texto = file.read()

caracteres_distintos = set(texto)
print(f"Cantidad de caracteres distintos: {len(caracteres_distintos)}")

palabras = texto.split()
palabras_distintas = set(palabras)
print(f"Cantidad de palabras distintas: {len(palabras_distintas)}")