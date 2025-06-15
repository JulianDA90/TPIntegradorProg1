import prueba

resultado1, tiempo1 = medir_tiempo(suma_iterativa, n)
resultado2, tiempo2 = medir_tiempo(suma_formula, n)
print(f"Suma Iterativa: Resultado={resultado1}, Tiempo={tiempo1:.8f} segundos")
print(f"Suma Fórmula: Resultado={resultado2}, Tiempo={tiempo2:.8f} segundos")