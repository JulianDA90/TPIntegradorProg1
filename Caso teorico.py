import time
import psutil
import os

# Función para obtener memoria usada (en MB)
def memoria_actual():
    process = psutil.Process(os.getpid())
    return process.memory_info().rss / 1024**2

# --- Funciones para cada caso de complejidad ---

def constante(lista):
    return lista[0]

def lineal(lista):
    total = 0
    for x in lista:
        total += x
    return total

def cuadratica(lista):
    contador = 0
    for i in lista:
        for j in lista:
            contador += 1
    return contador

#Para funcion logaritmica
def busqueda_binaria(lista, objetivo):
    inicio = 0
    fin = len(lista) - 1
    while inicio <= fin:
        medio = (inicio + fin) // 2
        if lista[medio] == objetivo:
            return medio
        elif lista[medio] < objetivo:
            inicio = medio + 1
        else:
            fin = medio - 1
    return -1

#Para funcion exponencial
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

# Función para medir tiempo y memoria usando psutil
def medir(func, *args, **kwargs):
    mem_inicio = memoria_actual()
    t_inicio = time.time()

    resultado = func(*args, **kwargs)

    t_fin = time.time()
    mem_fin = memoria_actual()

    tiempo = t_fin - t_inicio
    memoria = mem_fin - mem_inicio  # Memoria consumida en MB

    return resultado, tiempo, memoria

# --- Ejecutar y medir ---

lista_corta = list(range(1000))        # Para O(n²)
lista_larga = list(range(1_000_000))   # Para O(n) y O(log n)

res1, tiempo1, memoria1 = medir(constante, lista_larga)
res2, tiempo2, memoria2 = medir(lineal, lista_larga)
res3, tiempo3, memoria3 = medir(cuadratica, lista_corta)
res4, tiempo4, memoria4 = medir(busqueda_binaria, lista_larga, 987654)
res5, tiempo5, memoria5 = medir(fibonacci, 30)

print(f"O(1) - Constante: {tiempo1:.8f} s - Memoria consumida: {memoria1:.6f} MB")
print(f"O(n) - Lineal: {tiempo2:.8f} s - Memoria consumida: {memoria2:.6f} MB")
print(f"O(n²) - Cuadrática: {tiempo3:.8f} s - Memoria consumida: {memoria3:.6f} MB")
print(f"O(log n) - Logarítmica: {tiempo4:.8f} s - Memoria consumida: {memoria4:.6f} MB")
print(f"O(2^n) - Exponencial: {tiempo5:.8f} s - Memoria consumida: {memoria5:.6f} MB")