"""Calculadora de Estadísticas de Números
Escribe un programa que permita al usuario ingresar una lista de números y realice los
siguientes cálculos estadísticos:
1. Calcular la suma de los números.
2. Calcular el promedio de los números.
3. Encontrar el número mínimo y el número máximo de la lista.
4. Calcular la desviación estándar de los números.
El programa debe solicitar al usuario que ingrese la lista de números separados por espacios y
luego imprimir los resultados de los cálculos estadísticos."""

import math
suma = 0
prom = 0
menor = 0
mayor = 0
desviacionEstandar = 0

numeros = input("Ingrese la lista de números separados por espacios: ").split()
numeros = [float(numero) for numero in numeros]

suma = sum(numeros)
prom = suma / len(numeros)

menor = min(numeros)
mayor = max(numeros)

desviacionEstandar = math.sqrt(sum((numero - prom) ** 2 for numero in numeros) / len(numeros))

print("Resultados:")
print("Suma: " + str(suma))
print("Promedio: " + str(prom))
print("Mínimo: " + str(menor))
print("Máximo: " + str(mayor))
print("Desviación estándar: "+ str(desviacionEstandar))
