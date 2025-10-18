import tkinter as tk
ventana=tk.Tk()
ventana.title("Interfaz")
ventana.geometry("300x300")
lista=tk.Listbox(ventana,selectmode=tk.EXTENDED,
                 bg="deep sky blue",
                 fg="black",
                 font=("Roboto",12,"bold"),
                 highlightcolor="white",
                 selectbackground="yellow",
                 selectforeground="red",
                 relief="solid",
                 highlightthickness=2,
                 borderwidth=3,
                 activestyle="none",
                 cursor="hand2")
                
elementos=["Rojo","vERDE", "Amarillo", "Azul"]
lista.insert(0, *elementos)
lista.pack(fill=tk.BOTH,expand=True)
def mostrar_seleccion():
    seleccion=lista.curselection()#guarda la elecion
    elementos_seleccionados=[lista.get(i) for i in seleccion]#se cre una lista con los elemento selecionados
    print(f"Elementos seleccionados: {elementos_seleccionados}")#imprime la elecion

lista.bind("<<ListboxSelect>>", lambda evento: mostrar_seleccion())#cuando selecionamos un elemento llama a la funcion
lista.itemconfigure(1,selectbackground="blue", selectforeground="white")#modificar la configuracion de una opcion

ventana.mainloop()
