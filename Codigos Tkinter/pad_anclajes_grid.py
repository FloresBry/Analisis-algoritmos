import tkinter as tk
ventana=tk.Tk()
ventana.geometry("500x500")
#etiquetas
elemento1=tk.Label(ventana,text="Elemento 1", bg="lightblue")
elemento2=tk.Label(ventana,text="Elemento 2", bg="lightgreen")
elemento3=tk.Label(ventana,text="Elemento 3", bg="lightcoral")
elemento4=tk.Label(ventana,text="Elemento 4", bg="lightyellow")
elemento5=tk.Label(ventana,text="Elemento 5", bg="lightpink")
elemento6=tk.Label(ventana,text="Elemento 6", bg="lightgrey")
#GRID
elemento1.grid(row=0,column=0,sticky="nswe")
elemento2.grid(row=0,column=1,sticky="nsew")
elemento3.grid(row=1,column=0,sticky="nsew")
elemento4.grid(row=1,column=1,sticky="nsew")

#CONFIGURACION GRID
ventana.columnconfigure(0)
ventana.columnconfigure(1)
ventana.columnconfigure(2)
#nos permite modificar la localizacion de la aparicion de nuestra ventana grid
ventana.grid_anchor("sw")
#bucle
ventana.mainloop()