import tkinter as tk
ventana=tk.Tk()
ventana.geometry("400x400")
#tamanio minimo al que podemos encoger la ventana
ventana.minsize(400,400)
#tamanio maximo al que podemos agrandar la ventana
ventana.maxsize(600,600)
#etiquetas
elemento1=tk.Label(ventana,text="Elemento 1", bg="lightblue")
elemento2=tk.Label(ventana,text="Elemento 2", bg="lightgreen")
elemento3=tk.Label(ventana,text="Elemento 3", bg="lightcoral")
elemento4=tk.Label(ventana,text="Elemento 4", bg="lightyellow")
elemento5=tk.Label(ventana,text="Elemento 5", bg="lightpink")
elemento6=tk.Label(ventana,text="Elemento 6", bg="lightgrey")
#grid
elemento1.grid(row=0,column=0,sticky="nsew")
elemento2.grid(row=0,column=1,sticky="nsew")
elemento3.grid(row=0,column=2,sticky="nsew")
elemento4.grid(row=1,column=0,sticky="nsew")
elemento5.grid(row=1,column=1,sticky="nsew")
elemento6.grid(row=1,column=2,sticky="nsew")
#esto le da el responsive a las columnas
ventana.columnconfigure(0,weight=1,minsize=100)
ventana.columnconfigure(1,weight=1,minsize=100)
ventana.columnconfigure(2,weight=1,minsize=100)
#configuracion responsive a las filas
ventana.rowconfigure(0,weight=1,minsize=100)
ventana.rowconfigure(1,weight=1,minsize=100)

ventana.mainloop()
