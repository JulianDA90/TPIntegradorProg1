#Paquetes utilizados
import time
import psutil
import os

# Función para mostrar uso de memoria actual (en MB)
def memoria_actual():
    process = psutil.Process(os.getpid())
    memoria_mb = process.memory_info().rss / 1024 ** 2
    return memoria_mb

# Función para medir tiempo y memoria de un bloque (función pasada como parámetro)
def medir(func, *args, **kwargs):
    mem_inicio = memoria_actual()
    t_inicio = time.time()

    resultado = func(*args, **kwargs)

    t_final = time.time()
    mem_final = memoria_actual()

    tiempo = t_final - t_inicio
    memoria = mem_final - mem_inicio  # memoria consumida durante la ejecución

    return resultado, tiempo, memoria

# Funciones general
def calculos_imc(peso, altura):
    if altura == 0:
        return 0
    return round(peso / (altura ** 2), 2)

#funcion para caso logaritmico
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

#funcion para caso exponencial
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

# Casos a medir como funciones para facilitar la medición

def caso1_constante():
    peso = 97
    altura = 1.89
    return calculos_imc(peso, altura)

def caso2_lineal():
    personas_imc = [
        (89, 1.74),
        (67, 1.65),
        (103, 1.93) 
    ]
    resultados = []
    for peso, altura in personas_imc:
        resultados.append(calculos_imc(peso, altura))
    return resultados

def caso3_cuadratica():
    personas_imc = [
        (89, 1.74),
        (67, 1.65),
        (103, 1.93) 
    ]
    imcs = [calculos_imc(p, a) for p, a in personas_imc]
    resultados = []
    for i in range(len(imcs)):
        for j in range(len(imcs)):
            resultados.append(imcs[i] * imcs[j])
    return resultados

def caso4_logaritmica():
    datos_ordenados = list(range(0, 1000000, 2))
    return busqueda_binaria(datos_ordenados, 882)

def caso5_exponencial():
    return fibonacci(20)

# --- Medición ---

res1, tiempo1, mem1 = medir(caso1_constante)
res2, tiempo2, mem2 = medir(caso2_lineal)
res3, tiempo3, mem3 = medir(caso3_cuadratica)
res4, tiempo4, mem4 = medir(caso4_logaritmica)
res5, tiempo5, mem5 = medir(caso5_exponencial)

# --- Resultados ---

print("Resultados de análisis algorítmico:\n")

print(f"Caso 1 (Constante O(1))       - Tiempo: {tiempo1:.8f}s - Memoria: {mem1:.4f} MB")
print(f"Caso 2 (Lineal O(n))          - Tiempo: {tiempo2:.8f}s - Memoria: {mem2:.4f} MB")
print(f"Caso 3 (Cuadrática O(n²))     - Tiempo: {tiempo3:.8f}s - Memoria: {mem3:.4f} MB")
print(f"Caso 4 (Logarítmica O(log n)) - Tiempo: {tiempo4:.8f}s - Memoria: {mem4:.4f} MB")
print(f"Caso 5 (Exponencial O(2^n))   - Tiempo: {tiempo5:.8f}s - Memoria: {mem5:.4f} MB")