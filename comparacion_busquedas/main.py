import tkinter as tk
from tkinter import ttk, messagebox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
import time
import random
def busqueda_lineal(lista, x):
    for i, valor in enumerate(lista):
        if valor == x:
            return i
    return -1
def busqueda_binaria(lista, x):
    izquierda, derecha = 0, len(lista) - 1
    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        if lista[medio] == x:
            return medio
        elif lista[medio] < x:
            izquierda = medio + 1
        else:
            derecha = medio - 1
    return -1
def medir_tiempo(funcion, lista, valor):
    inicio = time.perf_counter()
    resultado = funcion(lista, valor)
    fin = time.perf_counter()
    tiempo_ms = (fin - inicio) * 1000
    return resultado, tiempo_ms
def generar_datos(tamaño):
    return sorted(random.sample(range(tamaño * 2), tamaño))
class BusquedaGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Comparación de Búsquedas")
        self.lista = []
        self.resultados = {}
        control_frame = ttk.Frame(root)
        control_frame.pack(pady=10)
        ttk.Label(control_frame, text="Tamaño de lista:").grid(row=0, column=0)
        self.tamaño_entry = ttk.Combobox(control_frame, values=[100, 1000, 10000, 100000])
        self.tamaño_entry.grid(row=0, column=1)
        self.generar_btn = ttk.Button(control_frame, text="Generar datos", command=self.generar)
        self.generar_btn.grid(row=0, column=2, padx=5)
        ttk.Label(control_frame, text="Valor a buscar:").grid(row=1, column=0)
        self.valor_entry = ttk.Entry(control_frame)
        self.valor_entry.grid(row=1, column=1)
        self.lineal_btn = ttk.Button(control_frame, text="Búsqueda lineal", command=self.buscar_lineal)
        self.lineal_btn.grid(row=1, column=2, padx=5)
        self.binaria_btn = ttk.Button(control_frame, text="Búsqueda binaria", command=self.buscar_binaria)
        self.binaria_btn.grid(row=1, column=3, padx=5)
        self.resultado_label = ttk.Label(root, text="Resultados aparecerán aquí")
        self.resultado_label.pack(pady=5)
        self.canvas_frame = ttk.Frame(root)
        self.canvas_frame.pack()
    def generar(self):
        try:
            tamaño = int(self.tamaño_entry.get())
            self.lista = generar_datos(tamaño)
            self.resultado_label.config(text=f"Lista generada con {tamaño} elementos.")
        except:
            messagebox.showerror("Error", "Tamaño inválido.")
    def buscar_lineal(self):
        self.buscar(busqueda_lineal, "lineal")
    def buscar_binaria(self):
        self.buscar(busqueda_binaria, "binaria")
    def buscar(self, algoritmo, nombre):
        if not self.lista:
            messagebox.showerror("Error", "Primero genera los datos.")
            return
        try:
            valor = int(self.valor_entry.get())
        except:
            messagebox.showerror("Error", "Valor inválido.")
            return
        resultado, tiempo = medir_tiempo(algoritmo, self.lista, valor)
        tamaño = len(self.lista)
        texto = f"Tamaño: {tamaño} | Resultado: {resultado if resultado != -1 else 'No encontrado'} | Tiempo: {tiempo:.3f} ms"
        self.resultado_label.config(text=texto)
        if tamaño not in self.resultados:
            self.resultados[tamaño] = {}
        self.resultados[tamaño][nombre] = tiempo
        self.actualizar_grafica()
    def actualizar_grafica(self):
        for widget in self.canvas_frame.winfo_children():
            widget.destroy()
        fig, ax = plt.subplots(figsize=(5, 4))
        tamaños = sorted(self.resultados.keys())
        tiempos_lineal = [self.resultados[t].get("lineal", 0) for t in tamaños]
        tiempos_binaria = [self.resultados[t].get("binaria", 0) for t in tamaños]
        ax.plot(tamaños, tiempos_lineal, label="Lineal", marker='o')
        ax.plot(tamaños, tiempos_binaria, label="Binaria", marker='o')
        ax.set_title("Comparación de tiempos")
        ax.set_xlabel("Tamaño de lista")
        ax.set_ylabel("Tiempo (ms)")
        ax.legend()
        ax.grid(True)
        canvas = FigureCanvasTkAgg(fig, master=self.canvas_frame)
        canvas.draw()
        canvas.get_tk_widget().pack()
if __name__ == "__main__":
    root = tk.Tk()
    app = BusquedaGUI(root)
    root.mainloop()