#propiedades de PACK
import tkinter as tk
root=tk.Tk()
root.title("Interfaces")
root.geometry("400x400")
#CREAMOS BOTONES
boton1=tk.Button(root,text="Noroeste").pack(anchor=tk.NW)
boton2=tk.Button(root,text="Norte 2").pack(anchor=tk.N)
boton3=tk.Button(root,text="Noreste 3").pack(anchor=tk.NE)
boton4=tk.Button(root,text="Oeste").pack(anchor=tk.W)
boton5=tk.Button(root,text="Centro").pack(anchor=tk.CENTER)
boton6=tk.Button(root,text="Este").pack(anchor=tk.E)
boton7=tk.Button(root,text="Suroeste").pack(anchor=tk.SW)
boton8=tk.Button(root,text="Sur").pack(anchor=tk.S)
boton9=tk.Button(root,text="Sureste").pack(anchor=tk.SE,expand=True)
botonEmpaquetar1=tk.Button(root,text="Boton 1")
botonEmpaquetar2=tk.Button(root,text="Boton 2")

#EMPAQUETAMOS BOTONES #decidimos con after u before cual se muestra primero 
botonEmpaquetar1.pack()
botonEmpaquetar2.pack(before=botonEmpaquetar1)#para decir que el boton 2 se muestre primero que el  primer boton el boton 1 ya debe estar empaquetado
#EXPANSION DE WIDGETS
etiqueta1=tk.Label(root,
                  text="Etiqueta expansible",
                  bg='black')
etiqueta2=tk.Label(root,
                  text="Etiqueta expansible 2",
                  bg='SpringGreen')
etiqueta1.pack(expand=True,fill="x")
etiqueta2.pack(expand=True,fill="both")
#etiqueta
etiqueta3=tk.Label(root,text="Etiqueta expansible 3",
                   bg="blue")
etiqueta4=tk.Label(root,
                  text="Arriba",
                  bg='green')
etiqueta5=tk.Label(root,
                  text="Abajo",
                  bg='red')
etiqueta6=tk.Label(root,
                  text="Izquierda",
                  bg='yellow')
etiqueta7=tk.Label(root,
                  text="Derecha",
                  bg='blue')
etiqueta1.pack(ipadx=100,ipady=50)
#usando propiedad side
etiqueta4.pack(side="top")
etiqueta5.pack(side="bottom")
etiqueta6.pack(side="left")
etiqueta7.pack(side="right")
root.mainloop()