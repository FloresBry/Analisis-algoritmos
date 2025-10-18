import matplotlib.pyplot as plt
import time
import random
tiempos_fuerza_bruta=[0]
tiempos_divide_venceras=[0]
tiempos_programacion_dinamica=[0]
tamaios=[0]
def permutas_programacion_dinamica(lista,memoria={}):
    # Verificar si la permutación ya está en la memoria
    if tuple(lista) in memoria:
        # Devolver la permutación almacenada
        return memoria[tuple(lista)]
    # Caso base: si la lista tiene un solo elemento, es una permutación.
    if len(lista) <= 1:
        return [lista]
    # Lista para almacenar todas las permutaciones
    permutas_totales=[]
    # Recorrer cada elemento de la lista
    for i in range(len(lista)):
        elemento_actual = lista[i]
        # Crear una sub-lista con los elementos restantes
        resto_de_la_lista = lista[:i] + lista[i+1:]
        # Llamada recursiva para obtener las permutaciones de la sub-lista
        permutaciones_del_resto = permutas_programacion_dinamica(resto_de_la_lista, memoria)
        # Iterar sobre las permutaciones de la sub-lista
        for p in permutaciones_del_resto:
            # Añadir el elemento actual al inicio de cada permutación del resto
            nueva_permutacion = [elemento_actual] + p
            permutas_totales.append(nueva_permutacion)
    # Almacenar la permutación en la memoria antes de devolverla
    memoria[tuple(lista)] = permutas_totales
    
    # Devolver todas las permutaciones encontradas
    return permutas_totales

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

def permutas_divide_venceras(lista):
    # Caso base: si la lista tiene un solo elemento, es una permutación.
    if len(lista) == 1:
        return [lista]
    permutas_totales=[]
    # Recorrer cada elemento de la lista
    for i in range(len(lista)):
        elemento_actual = lista[i]
        # Crear una sub-lista con los elementos restantes
        resto_de_la_lista = lista[:i] + lista[i+1:]
        # Llamada recursiva para obtener las permutaciones de la sub-lista
        permutaciones_del_resto = permutas_divide_venceras(resto_de_la_lista)
        # Iterar sobre las permutaciones de la sub-lista
        for p in permutaciones_del_resto:
            # Añadir el elemento actual al inicio de cada permutación del resto
            nueva_permutacion = [elemento_actual] + p
            permutas_totales.append(nueva_permutacion)
    return permutas_totales
def medir_tiempo(funcion, lista):
    inicio = time.time()
    funcion(lista)
    fin = time.time()
    return (fin - inicio)*1000
def graficar():
    global tiempos_fuerza_bruta
    global tiempos_divide_venceras
    global tiempos_programacion_dinamica
    global tamaios
    plt.plot(tamaios, tiempos_fuerza_bruta, marker='o', linestyle='-', color='red', label='Fuerza Bruta')
    plt.plot(tamaios, tiempos_divide_venceras, marker='o', linestyle='-', color='blue', label='Divide y Vencerás')
    plt.plot(tamaios, tiempos_programacion_dinamica, marker='o', linestyle='-', color='green', label='Programación Dinámica')
    plt.title('Comparación de tiempos de ejecución de algoritmos de permutaciones')
    plt.xlabel('Tamaño de la lista')
    plt.ylabel('Tiempo de ejecución (ms)')
    plt.legend()
    plt.grid()
    plt.show()
if __name__ == "__main__":
    for n in range(1, 9):
        lista = list(range(n))
        
        tiempo_ejecucion_fb = medir_tiempo(generador_permutas_fuerza_bruta, lista)
        tiempos_fuerza_bruta.append(tiempo_ejecucion_fb)
        
        tiempo_ejecucion_dv = medir_tiempo(permutas_divide_venceras, lista)
        tiempos_divide_venceras.append(tiempo_ejecucion_dv)
        
        tiempo_ejecucion_pd = medir_tiempo(permutas_programacion_dinamica, lista)
        tiempos_programacion_dinamica.append(tiempo_ejecucion_pd)
        
        tamaios.append(n)
        
        print(f"Tamaño de la lista: {n}, Tiempo Fuerza Bruta: {tiempo_ejecucion_fb:.4f} ms, Tiempo Divide y Vencerás: {tiempo_ejecucion_dv:.4f} ms, Tiempo Programación Dinámica: {tiempo_ejecucion_pd:.4f} ms")
    graficar()
    