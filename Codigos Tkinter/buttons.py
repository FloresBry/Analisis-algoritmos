import tkinter as tk
ventana=tk.Tk()
ventana.title("Hola a todos")
ventana.geometry("300x200")
#boton
ventana_secundaria=tk.Toplevel()
ventana_secundaria.geometry("300x600+14+200")

boton=tk.Button(ventana_secundaria,text="Haz clic",font=("Arial", 15, "bold"),
                bg='orange',
                fg='red',activeforeground='blue',
                activebackground='black',
                borderwidth=5,relief='sunken',bd=10,state='disabled',
                disabledforeground='white',cursor='cross')
boton.pack()


ventana.mainloop()

