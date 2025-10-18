import tkinter as tk
root=tk.Tk()
root.title("Geometria")
#dimensiones de la ventana
ancho=400
alto=75
#psoicion de la ventana
posicion_x=50
posicion_y=700
root.geometry(f"{ancho}x{alto}+{posicion_x}+{posicion_y}")

root.mainloop()