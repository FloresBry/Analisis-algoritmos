import tkinter as tk
def salud():
    print("Hola mundo")
    
def doble_clic_izquierdo(evento):
    print("Double click con el boton izquierdo")

#ventana.bind("<double-button-1>",doble_clic_izquierdo)
root=tk.Tk()
boton=tk.Button(root,text="haz clic aqui",command=salud)
boton.pack()
root.mainloop()