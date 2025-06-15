# Algoritmo 1: Suma iterativa
import time
import Utils

peso = 97
altura = 1.89

personas_imc = [
    (89, 1.74),
    (67, 1.65),
    (103, 1.93) 
]

#Caso 1, Constante

#inicio1 = Utils.medicion_inicial()
resultadoO1 = Utils.calculos_imc(peso, altura)
final1 = Utils.medicion_final()

#Caso 2, lineal

inicio2 = Utils.medicion_inicial()

for peso, altua in personas_imc:
    resultadoOn = Utils.calculos_imc(peso, altura)
    
final2 = Utils.medicion_final()

#Caso 3, Cuadratica

inicio3 = Utils.medicion_inicial()

imcs = [Utils.calculos_imc(p, a) for p, a in personas_imc]

for i in range(len(imcs)):
    for j in range(len(imcs)):
        pass


final3 = Utils.medicion_final()

print(final3)

