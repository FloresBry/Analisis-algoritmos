import tkinter as tk
root=tk.Tk()
root.title("Viendo entry")
root.geometry("300x400")
root.config(cursor="pirate")
entrada=tk.Entry(root,bg='blue',fg='orange',
                 border=10,relief='solid',cursor='pirate'
                 ,state='disabled')
entrada.config(cursor='star')
entrada.pack()

root.mainloop()

tk.Button()
tk.Entry()
tk.Label()