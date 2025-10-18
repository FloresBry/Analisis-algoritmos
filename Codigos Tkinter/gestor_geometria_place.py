#me srive par aposicionar widgets y que por default sean responsivos, osea todo lo que contengan sera responsivo
import tkinter as tk
ventana=tk.Tk()
ventana.title("Usando gestor place")
ventana.geometry("330x111")
elemento_1=tk.Label(ventana,text="elemento 1", bg="gold")
elemento_2=tk.Label(ventana,text="elemento 2", bg="blue")
elemento_3=tk.Label(ventana,text="elemento 3", bg="green")
elemento_4=tk.Label(ventana,text="elemento 4", bg="red")
#colocacion con el gestor place()
'''elemento_1.place(x=0,y=0,width=160,height=50)
elemento_2.place(x=170,y=0,width=160,height=50)
elemento_3.place(x=0,y=60,width=160,height=50)
elemento_4.place(x=170,y=60,width=160,height=50)'''
#posicionamiento relativo
elemento_1.place(relx=0,rely=0,relwidth=0.25,relheight=0.25)
elemento_2.place(relx=0.30,rely=0,relwidth=0.25,relheight=0.25)
elemento_3.place(relx=0,rely=0.30,relwidth=0.25,relheight=0.25)
elemento_4.place(relx=0.30,rely=0.30,relwidth=0.25,relheight=0.25)
ventana.mainloop()