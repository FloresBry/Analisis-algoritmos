import tkinter as tk
import random
import time
ANCHO=800
ALTO=300
datos=[]#lista global
root=tk.Tk()
root.title("Nuestro propio programa")
root.geometry("900x500")
canvas=tk.Canvas(root,width=800,height=300,background='white')
canvas.pack(padx=10,pady=10)

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

def hacer_barras(canvas,datos,activos=None):
    canvas.delete("all")

    n=len(datos)
    margen=10
    ancho_disp=ANCHO-2*margen
    alto_disp=ALTO-2*margen
    w=ancho_disp/n
    esc=alto_disp/max(datos)
    
    for i, v in enumerate(datos):
        x0=margen+i*w
        x1=x0+w*0.7
        h=v*esc
        y0=ALTO-margen-h
        y1=ALTO-margen
        color='blue'
        if activos and i in activos:
            color='yellow'
        canvas.create_rectangle(x0,y0,x1,y1,fill=color,outline='')
    canvas.create_text(6,6, anchor='nw',text=f'n={n}',fill='blue')

        
        
def generar():
    global datos
    random.seed(time.time())
    datos=[random.randint(5,100) for _ in range(200)]
    hacer_barras(canvas,datos)
    
def ordenar_selection():
    if not datos: return
    gen=selection_sort_steps(datos,lambda activos=None:hacer_barras(canvas,datos,activos))
    def paso ():
        try:
            next(gen)
            root.after(9,paso)
        except StopIterationto:
            pass
    paso()
panel=tk.Frame(root)
panel.pack(pady=6)
tk.Button(panel,text="Clicqueame",command=generar).pack(side='left',padx=5)
tk.Button(panel,text="adios",command=ordenar_selection).pack(side='left',padx=5)
generar()
root.mainloop()