
def es_palindromo(texto):
    # Convertir el texto a minúsculas y eliminar espacios y caracteres especiales
    texto_limpio = ''.join(char.lower() for char in texto if char.isalnum())
    
    # Verificar si el texto limpio es igual al texto invertido
    return texto_limpio == texto_limpio[::-1]

# Programa principal
if __name__ == "__main__":
    # Solicitar al usuario que ingrese un texto
    texto = input("Ingresa un texto para verificar si es un palíndromo: ")

    # Determinar si es un palíndromo
    if es_palindromo(texto):
        print("El texto ingresado es un Palíndromo")
    else:
        print("El texto ingresado No es un Palíndromo")
