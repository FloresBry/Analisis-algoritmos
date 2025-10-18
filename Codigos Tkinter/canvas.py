import tkinter as tk
from tkinter import ttk
window=tk.Tk()
window.geometry("600x500")
window.title('Canvas')
canvas=tk.Canvas(window, bg= 'lightblue')
canvas.pack()
canvas.create_rectangle((50,20,200,200),fill='red',width=2,dash=(10,6),outline='white')
canvas.create_line(0,0,150,100,fill="black")
canvas.create_oval(300,10,200,80,fill='green')
canvas.create_polygon(50,0,100,200,200,50,fill='white')
canvas.create_arc(300,10,200,80, 
                  fill='red', 
                  start=45,
                  extent=140,
                  style=tk.CHORD, 
                  outline='yellow',
                  width=3)
canvas.create_text(30,140, text="BRY canva basico",fill='gray', width=1)
canvas.create_window(150,100,window=ttk.Label(window, text="Esto es texto en el widget canvas"))
def draw_on_canvas(event):
    x=event.x
    y=event.y
    canvas.create_oval(x-brush_size/2,y-brush_size/2,x+brush_size/2,y+brush_size/2,fill="black")
brush_size=2
def brush_size_adjust(event):
    global brush_size
    if event.delta >0:
        brush_size+=4
    else:
        brush_size-=4
    brush_size=max(0,min(brush_size,50))
    
canvas.bind('<Motion>',draw_on_canvas)
canvas.bind('<MouseWheel>',brush_size_adjust)
window.mainloop()