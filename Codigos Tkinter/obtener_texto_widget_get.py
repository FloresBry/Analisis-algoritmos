import tkinter as tk
root=tk.Tk()
root.title("Obteniendo texto")
root.geometry("500x500")
texto=tk.Text(root, width=50, height=20)
texto.pack()
def obtener_texto():
    texto_obtenido=texto.get("1.0",'end')
    print(texto_obtenido)
def obtener_texto_selecionado():#se obtiene el texto que seleciona tu cursor
    seleccion=texto.get("sel.first",'sel.last')
    print(f"Un pequenio texto: {seleccion}")
def modificar_texto():#se modifica el texto selecionado por el cursor
    nuevo_texto="TEXTO MODIFICADO"
    texto.replace('sel.first','sel.last',nuevo_texto)
#funcion para imprimir la posicion del cursor
def posicion_cursor(evento):
    posicion=texto.index(tk.CURRENT)
    print(posicion)

    
boton_obtener_text=tk.Button(root,text="Guardar texto",command=obtener_texto)
boton_obtener_text.pack()
boton_obtener_text_selec=tk.Button(root,text='Guardar text selec',command=obtener_texto_selecionado)
boton_obtener_text_selec.pack()
boton_modificar_text=tk.Button(root,text="Modificar texto",command=modificar_texto)
boton_modificar_text.pack()
boton_obtener_posicion_cursor=tk.Button(root,text="Posicion cursor",command=posicion_cursor)
boton_obtener_posicion_cursor.pack()
#asociar las pulsaciones de teclas a la funcion
texto.bind("<KeyRelease>",posicion_cursor)
root.mainloop()
