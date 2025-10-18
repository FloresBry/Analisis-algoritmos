#Esto sirve para que sea dinamico en temas de distribucion de nuestros widgets
#podemos entender esto como si estuvieramos disenando las partes de una pagina
#grid nos dice en que parte ira cada una
#asi podemos distribuirlas
#esta pagina la guardo para ejemplificar como distribuir la partes de una interfaz
import tkinter as tk
ventana=tk.Tk()
ventana.title("Interfaces")
ventana.geometry("200x300")
#etiquetas
elemento_1=tk.Label(ventana,text="Elemento 1",bg="gold",width=28,height=10)
elemento_2=tk.Label(ventana,text="Elemento 2",bg="lightblue",width=28,height=10)
elemento_3=tk.Label(ventana,text="Elemento 3",bg="lightgreen",width=28,height=10)
elemento_4=tk.Label(ventana,text="Elemento 4",bg="lightpink",width=28,height=10)
elemento_5=tk.Label(ventana,text="Elemento 5",bg="gold",width=28)
elemento_6=tk.Label(ventana,text="Elemento 6",bg="lightblue",width=28)
elemento_7=tk.Label(ventana,text="Elemento 7",bg="lightgreen",width=28)
elemento_8=tk.Label(ventana,text="Elemento 8",bg="lightpink",width=28)
elemento_9=tk.Label(ventana, text="elemento 9",bg="violet",width=28)
#posicionamiento estamos ordenando el contenido de las filas 
elemento_1.grid(row=1,sticky="nsew")
elemento_2.grid(row=2,sticky="nsew")
elemento_3.grid(row=3,sticky="nsew")
elemento_4.grid(row=4,sticky="nsew")
#especificamos cuanto de la pantalla abarca nuestra fila que ordenamos, en cuestion a pixeles
ventana.rowconfigure(1,weight=1)
ventana.rowconfigure(2,weight=2)
ventana.rowconfigure(3,weight=1)
ventana.rowconfigure(4,weight=3)
#posicionamiento estamos acomodando las columnas para que sean dinamicas
elemento_5.grid(row=0,column=0,sticky="we")
elemento_6.grid(row=0,column=1,sticky="we")
elemento_7.grid(row=0,column=2,sticky="we")
elemento_8.grid(row=0,column=3,sticky="we")
#aqui estoy posicionando un cuadro que abarque 3 columnas y 4 filas para que sea una parte importante
elemento_9.grid(row=1,column=1,sticky="nsew",columnspan=3,rowspan=4)
#especificamos el comportamiento de las columnas, cuando hablamos de peso nos referimos a lo que abarcan de la interfaz en pixeles
ventana.columnconfigure(0,weight=1)
ventana.columnconfigure(1,weight=1)
ventana.columnconfigure(2,weight=1)
ventana.columnconfigure(3,weight=1)
#loop
ventana.mainloop()