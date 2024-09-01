
import random

# Generar lista de 10 números aleatorios del 1 al 100
numeros = [random.randint(1, 100) for _ in range(10)]

# Mostrar la lista de números generados
print("Lista de números generados:", numeros)

# Calcular el promedio de los números en el arreglo
promedio = sum(numeros) / len(numeros)
print("Promedio:", promedio)

# Función para verificar si un número es primo
def es_primo(num):
    if num <= 1:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    for i in range(3, int(num**0.5) + 1, 2):
        if num % i == 0:
            return False
    return True

# Contar números primos y pares, número mayor y número menor
cantidad_primos = sum(1 for numero in numeros if es_primo(numero))
cantidad_pares = sum(1 for numero in numeros if numero % 2 == 0)
numero_mayor = max(numeros)
numero_menor = min(numeros)

print("Cantidad de números primos:", cantidad_primos)
print("Cantidad de números pares:", cantidad_pares)
print("Número mayor:", numero_mayor)
print("Número menor:", numero_menor)
