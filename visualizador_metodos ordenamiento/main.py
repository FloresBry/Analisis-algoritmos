import tkinter as tk
from tkinter import ttk# para el dropbox
import matplotlib.pyplot as plt #Graficas
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg #graficas junto tkinter
import random
import time
ANCHO =800 # ancho del canvas
ALTO= 300# alto del canvas
N_BARRAS=40# cuantas barras se dibujan
VAL_MIN, VAL_MAX=5,100# rango de valores aleatorio para las barras
RETARDO_MS=0#velocidad de animacion en milisegundos
#funcion para terminar procesos de tkinter
def cerrar_ventana():
    root.quit()
    root.destroy()
#metodo de ordenamiento selection
def selection_sort_steps(data,draw_callback):
    n=len(data)#calcula tamanio de data
    for i in range(n):
        min_idx=i
        for j in range(i+1,n):
            draw_callback(activos=[i,j,min_idx]);yield
            if data[j]<data[min_idx]:
                min_idx=j
        data[i], data[min_idx]=data[min_idx],data[i]
        draw_callback(activos=[i,min_idx]);yield
    draw_callback(activos=[])
def bubblesort_steps(vectorbs,draw_callback):
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
                draw_callback(activos=[j,j+1]);yield
            # Se intercambian si el elemento encontrado es mayor 
            # Luego pasa al siguiente
    draw_callback(activos=[])
    #print ("El vector ordenado por el metodo burbuja es: ",vectorbs)
def mergesort_steps(vectormerge,call_back):
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
        
        i = j = k = 0
        if largo(vectormerge) >1: 
            medio = largo(vectormerge)//2# Buscamos el medio del vector
            #call_back(activos=[medio]);yield
            
            # Lo dividimos en 2 partes 
            izq = vectormerge[:medio]  
            der = vectormerge[medio:]
            
            yield from merge(izq) # Mismo procedimiento a la primer mitad
            yield from merge(der) # Mismo procedimiento a la segunda mitad
            
            
                
                # Copiamos los datos a los vectores temporales izq[] y der[] 
            while i < largo(izq) and j < largo(der): 
                call_back(activos=[i,j]);yield
                if izq[i] < der[j]: 
                    
                    vectormerge[k] = izq[i] 
                    call_back(activos=[k,i]);yield
                    i+= 1
                else: 
                    call_back(activos=[k,j]);yield
                    vectormerge[k] = der[j] 
                    j+= 1
                k += 1
                
            # Nos fijamos si quedaron elementos en la lista
            # tanto derecha como izquierda 
            while i < largo(izq): 
                call_back(activos=[i,k]);yield
                vectormerge[k] = izq[i] 
                i+= 1
                k+= 1
                
            while j < largo(der): 
                call_back(activos=[j,k]);yield
                vectormerge[k] = der[j] 
                j+= 1
                k+= 1
    yield from merge(vectormerge)
    call_back(activos=[])
    #print("El vector ordenado con merge es: ", vectormerge)
def quicksort_steps(vectorquick, start= 0):
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

#funcion dibujo
def dibujar_barras(canvas,datos,activos=None):
    canvas.delete("all")
    if not datos:return
    n=len(datos)
    margen=10
    ancho_disp=ANCHO-2*margen
    alto_disp=ALTO-2*margen
    w=ancho_disp/n
    esc=alto_disp/max(datos)
    for i,v in enumerate(datos):
        x0=margen+i*w
        x1=x0 +w*0.9
        h=v*esc
        y0=ALTO-margen-h
        y1=ALTO-margen
        color="#4e79a7"
        if activos and i in activos:
            color="#f28e2b"
        canvas.create_rectangle(x0,y0,x1,y1, fill=color,outline="")
    canvas.create_text(6,6, anchor="nw",text=f"n={len(datos)}",fill="#666")

#aplicacion principal
#estas son las opciones que se muestran en el dropbox combo
opciones_ordenamiento=['Selection Sort','Bubble Sort', 'Merge Sort', 'Quick Sort']
#listas necesarias para guardar informacion
datos=[]
listaTiemposbubble=list([0]) #definimos la lista tiempos como una lista
listaTiemposMerge=list([0])
listaTiemposQuick=list([0])
listaTiemposSelection=[0]
listaRangoBubble=[0]
listaRangoMerge=[0]
listaRangoQuick=[0]
listaRangoSelection=[0]

root=tk.Tk()
root.title("Visualizaro -selection sort")
canvas=tk.Canvas(root,width=ANCHO, height=ALTO, bg="white")
canvas.pack(padx=100, pady=10)

#haciendo graficas
fig, ax=plt.subplots(dpi=90, figsize=(7,5), facecolor='#00faafb7')

# se grafican y actualizan las graficas
def graficar_Datos():
    

    #lugares donde se guardan los datos
    global listaRangoSelection
    global listaTiemposSelection
    global listaRangoBubble
    global listaTiemposbubble
    global listaRangoMerge
    global listaTiemposMerge
    global listaRangoQuick
    global listaTiemposQuick
    #se limpia las etiquetas de la grafica
    ax.clear()
    #titulo y etiquetas
    plt.title("Grafica comparacion",color='blue',size=16,family='Arial')#titulo grafica
    ax.set_xlabel("Cantidad", color="black")#etiquetas en x
    ax.set_ylabel("tiempo",color='black')#etiquetas en y

    #se genera cada grafica
    ax.plot(listaRangoSelection,listaTiemposSelection,"o--", label="Selection Sort", color='blue')
    ax.plot(listaRangoBubble,listaTiemposbubble,"o--", label="Bubble Sort",color='red')
    ax.plot(listaRangoMerge,listaTiemposMerge,"o--", label="Merge Sort", color='yellow')
    ax.plot(listaRangoQuick,listaTiemposQuick,"o--", label="Quick Sort", color='black')
    #leyenda que muestra lo que significa cada grafica
    ax.legend(loc="upper left")
    #grafica cuadriculada
    ax.grid(True)
    #dibuja la grafica
    canvas_grafico.draw()
    canvas_grafico.get_tk_widget().pack()
    
    
    
def generar():
    global datos
    random.seed(time.time())
    datos=[random.randint(VAL_MIN, VAL_MAX) for _ in range(N_BARRAS)]
    dibujar_barras(canvas,datos)

def ordenar_selection():
    if not datos: return
    gen=selection_sort_steps(datos, lambda activos=None: dibujar_barras(canvas,datos,activos))
    def paso():
        try:
            next(gen)
            root.after(RETARDO_MS,paso)
        except StopIteration:
            pass
    paso()
def ordenar_bubble():
    if not datos: return
    gen=bubblesort_steps(datos, lambda activos=None: dibujar_barras(canvas,datos,activos))
    def paso():
        try:
            next(gen)
            root.after(RETARDO_MS,paso)
        except StopIteration:
            pass
    paso()
def ordenar_merge():
    if not datos: return
    gen=mergesort_steps(datos, lambda activos=None: dibujar_barras(canvas,datos,activos))
    def paso():
        try:
            next(gen)
            root.after(RETARDO_MS,paso)
        except StopIteration:
            pass
    paso()
def ordenar_quick():
    if not datos: return
    gen=quicksort_steps(datos, lambda activos=None: dibujar_barras(canvas,datos,activos))
    def paso():
        try:
            next(gen)
            root.after(RETARDO_MS,paso)
        except StopIteration:
            pass
    paso()
#mide el tiempo
def medir_tiempo_funciones_ordenamiento(funcion):
    inicio=time.time()
    funcion()
    final=time.time()
    return final-inicio
#hace la selecion de ordenamiento
def selecionar_ordenamiento():
    global listaRangoSelection
    global listaTiemposSelection
    global listaRangoBubble
    global listaTiemposbubble
    global listaRangoMerge
    global listaTiemposMerge
    global listaRangoQuick
    global listaTiemposQuick
    seleccion=combo.get()
    if seleccion=='Selection Sort':
        #se guarda la cantidad del entry
        listaRangoSelection.append(int(entrada_barras.get()))
        # se calcula el tiempo 
        listaTiemposSelection.append(medir_tiempo_funciones_ordenamiento(ordenar_selection))
        #impresiones para conocer los datos
        print(listaRangoSelection)
        print(listaTiemposSelection)
        
    elif seleccion=='Bubble Sort':
        listaRangoBubble.append(int(entrada_barras.get()))
        listaTiemposbubble.append(medir_tiempo_funciones_ordenamiento(ordenar_bubble))
        #impresiones para conocer los datos
        print(listaTiemposbubble)
        print(listaRangoBubble)
    elif seleccion=='Merge Sort':
        listaRangoMerge.append(int(entrada_barras.get()))
        listaTiemposMerge.append(medir_tiempo_funciones_ordenamiento(ordenar_merge))
        print(listaTiemposMerge)
        print(listaRangoMerge)
    else:
        listaRangoQuick.append(int(entrada_barras.get()))
        listaTiemposQuick.append(medir_tiempo_funciones_ordenamiento(ordenar_quick))
        print(listaTiemposQuick)
        print(listaRangoQuick)
    graficar_Datos()
#funcion para mezclar datos
def mezclar():
    global datos
    n=len(datos)
    for i in range(n):
        indice_aleatorio=random.randint(0,n-1)
        temporal=datos[i]
        datos[i]=datos[indice_aleatorio]
        datos[indice_aleatorio]=temporal
    dibujar_barras(canvas,datos)
#funcion para cambiar el numero de barras
def determinar_barras():
    global N_BARRAS
    numero_barras=int(entrada_barras.get())
    N_BARRAS=numero_barras
    print(N_BARRAS)
# cambiar velocidad del algoritmo
def cambiar_velocidad(valor):
    global RETARDO_MS
    print(valor)
    RETARDO_MS=valor

panel=tk.Frame(root)
panel.pack(pady=6)
#boton generar numeros aleatorios
boton_generar=tk.Button(panel,text="Generar", command= generar)
boton_generar.pack(side='left',padx=5)
#botton para mezclar
boton_mezclar=tk.Button(panel,text='Mezclar',command=mezclar)
boton_mezclar.pack(side ="left",pady=10,padx=30)
#boton ordenar lista de numeros
boton_ordenar=tk.Button(panel,text="Ordenar ", command= selecionar_ordenamiento)
boton_ordenar.pack(side='left') 
#Creacion del dropbox
combo=ttk.Combobox(panel,values=opciones_ordenamiento, state="readonly")
combo.pack(pady=10,side='left')#enpaqutado del dropbox
combo.current(0)#opcion por defecto selection sort

#nuevo panel para escoger las barras
panel_bottom=tk.Frame(root)
panel_bottom.pack(pady=6)
#texto para decirle al usuario que esta haciendo
texto_entrada_barras=tk.Label(panel_bottom,text="Introduce el numero de barras")
texto_entrada_barras.pack(pady=10,side='left')
#entrada de datos ENTRY
entrada_barras=tk.Entry(panel_bottom)
entrada_barras.insert(0,'40')#valor por default
entrada_barras.pack(side="left")
#boton para confirmar los datos
boton_barras=tk.Button(panel_bottom,text="Confirmar",command=determinar_barras)
boton_barras.pack(side="left",padx=10)
#texto para Velocidad
texto_velocidad=tk.Label(panel,text="Velocidad(0ms-200ms)")
texto_velocidad.pack(padx=30)
#Scale de velocidad
escala_velocidad=tk.Scale(panel,from_=0,to=200,showvalue=False,orient='horizontal',command=cambiar_velocidad)
escala_velocidad.pack(padx=30)
#botton para limpiar resaltados
boton_limpiar_resaltado=tk.Button(panel_bottom, text="Limpiar Resaltado")
boton_limpiar_resaltado.pack(pady=10)
#panel para graficos con canvas
panel_grafico=tk.Frame(root)
panel_grafico.pack(pady=10)
#definimos grafico
canvas_grafico=FigureCanvasTkAgg(fig, master=panel_grafico)

generar()
#para que se pueda cerrar la ventana
root.protocol("WM_DELETE_WINDOW",cerrar_ventana)
root.mainloop()