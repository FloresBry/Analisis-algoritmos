import tkinter as tk
ventana=tk.Tk()
ventana.title("Python: interfaces graficas")
#tamanio ventana
ancho=300
alto=300
#ventana.geometry(f"{ancho}x{alto}")
#estado de la ventana

ventana.wm_state("zoomed")#pantalla maximizada
ventana.wm_state("normal")#pantalla por defecto
ventana.wm_state("iconic")#pantalla escondida en la barra de tareas
ventana.wm_state("withdrawn")#oculta la venta que esta en segundo plano
ventana.wm_state("normal")
ventana.wm_state("icon")
#bucle de la ventana
ventana.mainloop()