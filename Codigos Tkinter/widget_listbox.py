import tkinter as tk
ventana=tk.Tk()
ventana.title("List box")
ventana.geometry("500x200")
#crear el widget listbox
lista=tk.Listbox(ventana,selectmode=tk.MULTIPLE)
lista2=tk.Listbox(ventana,selectmode=tk.EXTENDED)


#lista de elementos
elementos=["Rojo", "Azul", "Amarillo","Naranja"]#pudede ser una tupla
#insertar elementos en el listbox
lista.insert(0,"Elemento 1")
lista.insert(1,"elemento 2")
lista.insert(2,"elemento 3")
lista.pack(pady=10)#margen superior
#otra forma
lista2.insert(0,*elementos)
lista2.pack(pady=10)
cantidadElementos=lista2.size()
print(f"la lista tiene {cantidadElementos} elementos")

ventana.mainloop()