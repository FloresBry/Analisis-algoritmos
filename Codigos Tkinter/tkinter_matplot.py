import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
from random import sample
listNum=[14,22,32,45,12,53,62]
listCategorias=[1,2,3,4,5,6,7]



fig1, ax1=plt.subplots()
ax1.bar(listCategorias,listNum)
root=tk.Tk()
root.title("Dashboard")
root.geometry("800x800")
frame=tk.Frame(root)
frame.pack(fill='both')
canvas1=FigureCanvasTkAgg(fig1,frame)
canvas1.draw()
canvas1.get_tk_widget().pack(side='left', fill='both')
# Botón para cerrar la ventana correctamente
btn_salir = tk.Button(root, text="Cerrar", command=root.destroy)
btn_salir.pack(side='bottom', pady=10)
root.mainloop()
