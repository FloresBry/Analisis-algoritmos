import tkinter as tk
#ventana
root=tk.Tk()
root.title("Bloquear redimension")
#tamanio
ancho=300
alto=300
root.geometry(f"{ancho}x{alto}")
#impide redimension
root.resizable(True,False)
#bucle de la ventana
root.mainloop()