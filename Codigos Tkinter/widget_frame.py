#
import tkinter as tk
root=tk.Tk()
root.title("Interfaces graficas")
root.geometry("500x500")
#creamos los marcos
marco=tk.Frame(root)
marco1=tk.Frame(root)
marco2=tk.Frame(root)
marco3=tk.Frame(root)
marco4=tk.Frame(root)
#configuramos los amrcos
marco.config(bg="plum4",
             border=3,
             relief="sunken",
             width=200,
             height=200,
             cursor="cross")
marco1.config(bg="RoyalBlue",
             border=2,
             relief="solid",
             width=200,
             height=200,
             cursor="cross")
marco2.config(bg="cadetBlue1",
             border=3,
             relief="sunken",
             width=200,
             height=200,
             cursor="cross")
marco3.config(bg="coral",
             border=2,
             relief="solid",
             width=200,
             height=200,
             cursor="cross")
marco4.config(bg="sea green",
             border=2,
             relief="solid",
             width=200,
             height=200,
             cursor="cross")

#mostramos los marcos
marco.pack()
marco1.pack()
marco2.pack()
marco3.pack()
marco4.pack()
#botones
Boton_1=tk.Button(marco,text="Pulsame si te atreves")
Boton_1.pack()
Boton_2=tk.Button(marco2,text="soy el segundo boton")
Boton_2.pack()
#bucle
root.mainloop()