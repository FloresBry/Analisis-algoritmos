#librerias

import numpy as np
from random import sample
import time
import matplotlib.pyplot as plt

#FUNCIONES

#metodos de ordenamiento (funcionan solo con objetos tipo lista)
def bubblesort(vectorbs):
    """Esta función ordenara el vector que le pases como argumento con el Método de Bubble Sort"""
    
    # Imprimimos la lista obtenida al principio (Desordenada)
    #print("El vector a ordenar por el metodo burbuja es:",vectorbs)
    n = 0 # Establecemos un contador del largo del vector
    
    for _ in vectorbs:
        n += 1 #Contamos la cantidad de caracteres dentro del vector
    
    for i in range(n-1): 
    # Le damos un rango n para que complete el proceso. 
        for j in range(0, n-i-1): 
            # Revisa la matriz de 0 hasta n-i-1
            if vectorbs[j] > vectorbs[j+1] :
                vectorbs[j], vectorbs[j+1] = vectorbs[j+1], vectorbs[j]
            # Se intercambian si el elemento encontrado es mayor 
            # Luego pasa al siguiente
    #print ("El vector ordenado por el metodo burbuja es: ",vectorbs)
def mergesort(vectormerge):
    """Esta función ordenara el vector que le pases como argumento 
    con el Método Merge Sort"""
    
    # Imprimimos la lista obtenida al principio (Desordenada)
    #print("El vector a ordenar con merge es:", vectormerge)
    
    def merge(vectormerge):
    
        def largo(vec):
            largovec = 0 # Establecemos un contador del largovec
            for _ in vec:
                largovec += 1 # Obtenemos el largo del vector
            return largovec
        
        
        if largo(vectormerge) >1: 
            medio = largo(vectormerge)//2 # Buscamos el medio del vector
            
            # Lo dividimos en 2 partes 
            izq = vectormerge[:medio]  
            der = vectormerge[medio:]
            
            merge(izq) # Mismo procedimiento a la primer mitad
            merge(der) # Mismo procedimiento a la segunda mitad
            
            i = j = k = 0
            
            # Copiamos los datos a los vectores temporales izq[] y der[] 
            while i < largo(izq) and j < largo(der): 
                if izq[i] < der[j]: 
                    vectormerge[k] = izq[i] 
                    i+= 1
                else: 
                    vectormerge[k] = der[j] 
                    j+= 1
                k += 1
            
            # Nos fijamos si quedaron elementos en la lista
            # tanto derecha como izquierda 
            while i < largo(izq): 
                vectormerge[k] = izq[i] 
                i+= 1
                k+= 1
            
            while j < largo(der): 
                vectormerge[k] = der[j] 
                j+= 1
                k+= 1
    merge(vectormerge)
    #print("El vector ordenado con merge es: ", vectormerge)
def quicksort(vectorquick, start= 0):
    end = (len(vectorquick) - 1)
    """Esta función ordenara el vector que le pases como argumento con el Método Quick Sort"""
    
    # Imprimimos la lista obtenida al principio (Desordenada)
    #print("El vector a ordenar con quick es:", vectorquick)
    
    def quick(vectorquick, start = 0, end = len(vectorquick) - 1):
        
        
        if start >= end:
            return

        def particion(vectorquick, start = 0, end = len(vectorquick) - 1):
            pivot = vectorquick[start]
            menor = start + 1
            mayor = end

            while True:
                # Si el valor actual es mayor que el pivot
                # está en el lugar correcto (lado derecho del pivot) y podemos 
                # movernos hacia la izquierda, al siguiente elemento.
                # También debemos asegurarnos de no haber superado el puntero bajo, ya que indica 
                # que ya hemos movido todos los elementos a su lado correcto del pivot
                while menor <= mayor and vectorquick[mayor] >= pivot:
                    mayor = mayor - 1

                # Proceso opuesto al anterior            
                while menor <= mayor and vectorquick[menor] <= pivot:
                    menor = menor + 1

                # Encontramos un valor sea mayor o menor y que este fuera del arreglo
                # ó menor es más grande que mayor, en cuyo caso salimos del ciclo
                if menor <= mayor:
                    vectorquick[menor], vectorquick[mayor] = vectorquick[mayor], vectorquick[menor]
                    # Continua el bucle
                else:
                    # Salimos del bucle
                    break

            vectorquick[start], vectorquick[mayor] = vectorquick[mayor], vectorquick[start]
            
            return mayor
        
        p = particion(vectorquick, start, end)
        quick(vectorquick, start, p-1)
        quick(vectorquick, p+1, end)
        
    quick(vectorquick)
    #print("El vector ordenado con quick es:", vectorquick)

#------------------------
def generadorNumerosNp(cantidad):#generar numeros con nampy (crea un array)
    global listaArray
    listaArray=np.random.randint(0,99,cantidad)
#generar  vectores con sample lista (crea una lista) 
def generarNumerosSample(rango,cantidad):
    global listaNum
    listaNum=list(range(rango))
    listaNum=sample(listaNum,cantidad)
#mide el tiempo que tarda una funcion en procesarse
def medirtiempoFuncionesOrdenamiento(funcion,listaUsar):
    inicio=time.time()
    funcion(listaUsar)
    final=time.time()
    return final-inicio
#Aqui tenemos las diferentes formas de ordenamiento
def ordenador(listaUsar, algoritmo):
    algoritmo=algoritmo.lower()
    global listaTiemposbubble
    global listaTiemposmerge 
    global listaTiemposquick
    if algoritmo=="bubblesort":
        listaTiemposbubble.append(medirtiempoFuncionesOrdenamiento(bubblesort,listaUsar))
    elif algoritmo=="mergesort":
        listaTiemposmerge.append(medirtiempoFuncionesOrdenamiento(mergesort,listaUsar))
    elif algoritmo=="quicksort":
        listaTiemposquick.append(medirtiempoFuncionesOrdenamiento(quicksort,listaUsar))
    else:
        print("Opcion no valida")

def graficarDatos():#funcion para graficar datos
    global listaTiemposbubble
    global listaTiemposmerge
    global listaTiemposquick
    global listaRangosX
    plt.figure(figsize=(7,5))
    plt.plot(listaRangosX,listaTiemposbubble,"--",label="BubbleSort",color="blue",lw=2,ms=1)
    plt.plot(listaRangosX,listaTiemposmerge,"--",label="MergeSort",color="gray",lw=2)
    plt.plot(listaRangosX,listaTiemposquick,"--",label="QuickSort",color="red",lw=2)
    plt.legend(loc="upper left", fontsize=8,ncol=12,edgecolor='indigo')
    plt.title(" Comparando Metodos Ordenamiento")
    plt.xlabel("Cantidad de elementos",fontsize=10)
    plt.ylabel("Tiempo(s)",fontsize=10)
    plt.xlim(0,1000)
    plt.tick_params(axis="both",labelsize=10)
    plt.grid(True)
    plt.show()


#funcionamiento principal (MAIN)

#variables globales
listaTiemposbubble=list([]) #definimos la lista tiempos como una lista
listaTiemposmerge=list([])
listaTiemposquick=list([])
listaArray=np.ndarray#definimos la lista como un array nampy (NO SE USA EN EL PROGRAMA)
listaNum=list #lista donde generamos los numeros
listaRangosX=np.arange(0,1050,50) #generamos una lista con numero de 0 a 1000 en 50 a 50

for rango in listaRangosX:
    
    generarNumerosSample(1000,rango)
    ordenador(listaNum,"bubblesort")
    generarNumerosSample(1000,rango)
    ordenador(listaNum,"mergesort")
    generarNumerosSample(1000,rango)
    ordenador(listaNum,"quicksort")

graficarDatos()
