import tkinter as tk
#creacion y configuracion de la ventana
#se crea el objeto de ventana principal
ventana=tk.Tk()
#titurlo de la ventana
ventana.title("Hola A TODOS")
#establecer tamanio de la ventana
ventana.geometry('300x300')
#CODIGO IMPORTANTE
#fuente personalizada
fuenteNormal=('Roboto',10,'normal')
fuenteNegrita=('Impact',10,'bold')
fuenteCursiva=('Times',10,'italic')
fuenteSubrayado=('Calibri',10,'underline')
fuenteTachado=('Arial',10,'overstrike')
#etiqueta
etiqueta1=tk.Label(text='Fuente normal', bg='pink', fg='red', bd=24,cursor='hand2',disabledforeground='black',font=fuenteNormal)
etiqueta2=tk.Label(text='Fuente Negrita', bg='pink', fg='red', bd=24,cursor='hand2',disabledforeground='black',font=fuenteNegrita)
etiqueta3=tk.Label(text='Fuente Cursiva', bg='pink', fg='red', bd=24,cursor='hand2',disabledforeground='black',font=fuenteCursiva)
etiqueta4=tk.Label(text='Fuente subrayado', bg='pink', fg='red', bd=24,cursor='hand2',disabledforeground='black',font=fuenteSubrayado)
etiqueta5=tk.Label(text='Fuente tachado', bg='pink', fg='red', bd=24,cursor='hand2',disabledforeground='black',font=fuenteTachado)
#muetra la etiqueta en la ventana
etiqueta1.pack()
etiqueta2.pack()
etiqueta3.pack()
etiqueta4.pack()
etiqueta5.pack()
#bluce de la ventana
ventana.mainloop()

