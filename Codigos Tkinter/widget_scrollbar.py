#barra de desplazamineot
import tkinter as tk
ventana = tk.Tk()
ventana.title("Interfaz")
ventana.geometry("200x200")
scrollbarVertical=tk.Scrollbar(ventana)
scrollbarHorizontal=tk.Scrollbar(ventana,orient="horizontal")
scrollbarVertical.pack(side="right",fill="y")
scrollbarHorizontal.pack(side='bottom',fill='x')
#creamos texto
texto=tk.Text(ventana,wrap="none",yscrollcommand=scrollbarVertical.get,xscrollcommand=scrollbarHorizontal.set)#este comando actualiza scrollbar cuando se alarga el contenido
texto.pack(side="left",fill="both", expand=True)
scrollbarVertical.config(command=texto.yview)# cuando mueves la scroll  bar puedes ver el contenido
scrollbarHorizontal.config(command=texto.xview)
ventana.mainloop()