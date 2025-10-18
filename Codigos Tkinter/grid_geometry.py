#grid acomoda en filas y columnas
import tkinter as tk
ventana=tk.Tk()
ventana.title("Intefaz de python")
ventana.geometry("500x100")
#etiquetas formadas con grid columspan y rowspan,sctiky
elemento_1=tk.Label(ventana,text="Elemento 1", bg="gold",width=10,height=3)
elemento_2=tk.Label(ventana,text="Elemento 2", bg="lightblue",width=10,height=3)
elemento_3=tk.Label(ventana,text="Elemento 3", bg="lightgreen",width=10,height=3)
elemento_4=tk.Label(ventana,text="Elemento 4", bg="lightpink",width=10,height=3)
elemento_5=tk.Label(ventana,text="Elemento 5", bg="red",width=10,height=3)
elemento_6=tk.Label(ventana,text="Elemento 6", bg="yellow",width=10,height=3)
elemento_7=tk.Label(ventana,text="Elemento 7", bg="yellow",width=10,height=3)
#posicionamiento de etiquetas
"""elemento_1.grid(row=0,column=0)
elemento_2.grid(row=0,column=1,rowspan=3,sticky="ns")
elemento_3.grid(row=0,column=2)
elemento_4.grid(row=1,column=0)
elemento_5.grid(row=1,column=2)
elemento_6.grid(row=2,column=0)
elemento_7.grid(row=3,column=1)"""
#otro ejemplo
elemento_8=tk.Label(ventana,text="Elemento 1", bg="gold",width=10,height=3)
elemento_9=tk.Label(ventana,text="Elemento 2", bg="lightblue",width=10,height=3)
elemento_10=tk.Label(ventana,text="Elemento 3", bg="lightgreen",width=10,height=3)
#posicionamiento de etiquetas
elemento_1.grid(row=0,column=0)
elemento_2.grid(row=0,column=1)
elemento_3.grid(row=1,column=0,columnspan=2,sticky="we")
ventana.mainloop()