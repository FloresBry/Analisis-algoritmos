import tkinter as tk
root=tk.Tk()
root.title("Widget text")
root.geometry("300x300")

#widget text
texto=tk.Text(root,bg="cyan",font=("Calibri",14),
              fg='darkOliveGreen4',cursor='pencil')
texto.config(width=25, height=10)
texto.pack()
#aniade texto en una posicion que le pidas ("linea.caracter")
texto.insert("1.0","Primera linea\n")
texto.insert("2.0","Segunda linea\n")
texto.insert("3.0","Tercera linea\n")

#funcion para insertar texto en el widget Text
def insertar_texto():

    texto.insert("2.3","TEXTO ANIADIDO\n")

#funcion para eliminar texto
def eliminar_texto():
    texto.delete("1.0", tk.END)
#boton para llamar a la funcion de inserccion de texto Y Eliminar texto
boton_insertar=tk.Button(root,text="Insertar texto",command=insertar_texto)
boton_insertar.pack()
boton_eliminar=tk.Button(root,text="Eliminar texto",command=eliminar_texto)
boton_eliminar.pack()
root.mainloop()

#AMBITO GLOBAL
variable=0
print(variable)

def pruebas():
    #AMBITO LOCAL
    global variable
    variable=10
   
pruebas()
print(variable)