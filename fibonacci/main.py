# fibonacci.py
import numpy as np
from random import sample
import time
import matplotlib.pyplot as plt
import tkinter as tk
import tkinter.messagebox as messagebox
import tracemalloc
# Función Fibonacci recursiva
def fibonacci(n):
    if n==0:
        return 0    
    elif n==1:
        return 1    
    
    else:
        return fibonacci(n-1) + fibonacci(n-2)  
# Función Fibonacci con programación dinámica
def fibonacci_programacion_dinamica(n, memoria={}):
    if n in memoria:
        return memoria[n]
    elif n==0:
        return 0    
    elif n==1:
        return 1
    else:
        memoria[n] = fibonacci_programacion_dinamica(n-1, memoria) + fibonacci_programacion_dinamica(n-2, memoria)
        return memoria[n]
# Medir tiempo de ejecución
def medir_tiempo(funcion, n):
    inicio = time.perf_counter()
    resultado = funcion(n)
    fin = time.perf_counter()
    tiempo_ms = (fin - inicio) * 1000
    return resultado, tiempo_ms
# Graficar complejidad temporal
def graficar_fibonacci_complejidad_temporal(n):
    # Valores de n
    ns = list(range(n + 1))
    tiempos_recursivo = []
    tiempos_dinamico = []
    # Medir tiempos para cada n
    for i in ns:
        _, tiempo_recursivo = medir_tiempo(fibonacci, i)
        _, tiempo_dinamico = medir_tiempo(fibonacci_programacion_dinamica, i)
        tiempos_recursivo.append(tiempo_recursivo)
        tiempos_dinamico.append(tiempo_dinamico)
    # Graficar resultados
    plt.figure(figsize=(6, 6))
    plt.plot(ns, tiempos_recursivo, label='Recursivo', marker='o')
    plt.plot(ns, tiempos_dinamico, label='Programación Dinámica', marker='o')
    plt.xlabel('n (posición en la secuencia Fibonacci)')
    plt.ylabel('Tiempo (ms)')
    plt.title('Comparación de Complejidad Temporal de Fibonacci')
    plt.legend()
    plt.grid(True)
    plt.show()  
# Graficar complejidad espacial
def medir_memoria(funcion, n):
    # Iniciar seguimiento de memoria
    tracemalloc.start()
    # Ejecutar la función
    funcion(n)
    # Obtener el pico de memoria utilizado  
    _, pico = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    return pico / 1024  # Convertir a KB    
# Graficar complejidad espacial
def graficar_comparacion_complejidad_espacial(n):
    ns = list(range(n + 1))
    memoria_recursivo = []
    memoria_dinamico = []
    # Medir memoria para cada n
    for i in ns:
        pico_recursivo = medir_memoria(fibonacci, i)
        pico_dinamico = medir_memoria(fibonacci_programacion_dinamica, i)
        memoria_recursivo.append(pico_recursivo)
        memoria_dinamico.append(pico_dinamico)
    # Graficar resultados
    plt.figure(figsize=(6, 6))
    plt.plot(ns, memoria_recursivo, label='Recursivo', marker='o')
    plt.plot(ns, memoria_dinamico, label='Programación Dinámica', marker='o')
    plt.xlabel('n (posición en la secuencia Fibonacci)')
    plt.ylabel('Memoria (KB)')
    plt.title('Comparación de Complejidad Espacial de Fibonacci')
    plt.legend()
    plt.grid(True)
   
    plt.show()
if __name__ == "__main__":
    # Interfaz gráfica con Tkinter
    root=tk.Tk()
    root.title("Comparación de Fibonacci")
    root.geometry("600x300")
    frame=tk.Frame(root)
    frame.pack(pady=20) 
    # Elementos de la interfaz
    label=tk.Label(frame, text="Comparación de Fibonacci: Recursivo vs Programación Dinámica", font=("Arial", 14))
    label.pack(pady=10)
    message=tk.Label(frame, text="Ingrese el valor máximo de n para graficar:", font=("Arial", 10))
    message.pack(pady=5)
    # Entrada de valor n
    entrada=tk.Entry(frame)
    entrada.pack(pady=5)
    entrada.insert(0, "30")
    # Botones para graficar
    boton_graficar_temporal=tk.Button(frame, text="Graficar Complejidad Temporal", command=lambda: graficar_fibonacci_complejidad_temporal(int(entrada.get())))
    boton_graficar_temporal.pack(pady=5)    
    boton_graficar_espacial=tk.Button(frame, text="Graficar Complejidad Espacial", command=lambda: graficar_comparacion_complejidad_espacial(int(entrada.get())))
    boton_graficar_espacial.pack(pady=5)

    root.mainloop()
