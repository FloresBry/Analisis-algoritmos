#este codigo abre las ventanas de tkinter en medio, no importa el tamanio
import tkinter as tk
#ventana
ventana=tk.Tk()
ventana.title("Python: Interfaces graficas")
#obteniendo el ancho y alto de la pantlla del dispositivo
ancho_pantalla=ventana.winfo_screenwidth()
alto_pantalla=ventana.winfo_screenheight()
#imprimir dimensiones de pantalla (no necesario)
print(f"Ancho de la pantalla: {ancho_pantalla} pixeles")
print(f"Alto de la pantalla: {alto_pantalla} pixeles")
#establece el tamanio de la ventana
ancho_ventana=500
alto_ventana=300
#calcula la posicion x e y para centrar la ventana
posicion_x=round(ancho_pantalla/2 - ancho_ventana /2)
posicion_y=round(alto_pantalla/2 - alto_ventana /2)-30
#imprimir posiciones calculadas
print(f"Posicione X para centrar la ventana: {posicion_x} pixeles")
print(f"Posicione y para centrar la ventana: {posicion_y} pixeles")
#configura la geometria de la ventana
ventana.geometry(f"{ancho_ventana}x{alto_ventana}+{posicion_x}+{posicion_y}")
ventana.mainloop()