import tkinter
import tkinter.ttk
p=tkinter.Tk()
p.geometry("800x600+0+0")
p.title("Mario Bros")
canvas0=tkinter.Canvas(p,width=800,height=670)
imagen=tkinter.PhotoImage(file='Menu.gif')
canvas0.create_image(400,330, image=imagen)
canvas0.focus_set()
canvas0.pack()
p.withdraw()
def abrirjuego():
    global p
    o=tkinter.Toplevel(p)
    canvas1=tkinter.Canvas(o,width=800,height=600)
    menu=tkinter.PhotoImage(file='Mario.gif')
    canvas1.create_image(400,335,image=menu)
    canvas1.focus_set()
    canvas1.pack()
    def botonstart():
        p.iconify
        o.withdraw()
    Boton=tkinter.Button(o,text="w",command=abrirjuego)
    Boton.place(x=300,y=335)
    o.resizable(0,0)
    o.mainloop()
abrirjuego()
p.resizable
p.mainloop()

