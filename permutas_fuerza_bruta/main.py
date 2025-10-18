import matplotlib.pyplot as plt
import numpy as np
import time
import random
tiempos=[0]
tamanios=[0]

def factorial(n):
    if n < 0:
        return 0
    if n == 0:
        return 1
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado
def generador_permutas_fuerza_bruta(lista):
    permutas=[]
    n = len(lista)
    permutas.append(list(lista))
    while len(permutas) < factorial(n):
        nueva_lista = list(lista)
        random.shuffle(nueva_lista)
        
        if nueva_lista not in permutas:
            permutas.append(nueva_lista)
    return permutas
def medir_tiempo(func, args ):
    start_time = time.time()
    func(args)
    end_time = time.time()
    tiempo_total = end_time - start_time
    return tiempo_total*1000

def graficar():
    global tiempos
    global tamanios
    plt.plot(tamanios, tiempos, marker='o', linestyle='-', color='b')
    plt.xlabel('Tamaño de la lista (n)')
    plt.ylabel('Tiempo de ejecución (ms)')
    plt.title('Tiempo de ejecución de generación de permutaciones por fuerza bruta')
    plt.grid()
    plt.show()
    
if __name__=="__main__":
    listas_prueba = []
    for i in range(35):
        listas_prueba.append(i)
        tiempos.append(medir_tiempo(generador_permutas_fuerza_bruta, listas_prueba))
        tamanios.append(len(listas_prueba))
        print(f"Tamaño de la lista: {len(listas_prueba)}, Tiempo de ejecución: {tiempos[-1]} ms")
        input("Presiona Enter para continuar con el siguiente tamaño...")
        
    
 
 
