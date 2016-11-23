from tkinter import *
#Ventana y botones:
ventana = Tk()
ventana.title('Mario Bros')
ventana.geometry("800x600")

Playername=Label(ventana,text="Player Name: ")
Playername.place(x=300,y=300)

variable_string = StringVar()
cajadetexto = Entry(ventana,textvariable=variable_string)
cajadetexto.place(x=400,y=300)

botonstart = Button(ventana,text="Start",bg='Brown',relief=SOLID)
botonstart.place(x=400,y=350)

boton1player = Button(ventana,text="1 Player",bg='Red',relief=SOLID)
boton1player.place(x=200,y=500)

boton2players = Button(ventana,text="2 Players",bg='Green',relief=SOLID)
boton2players.place(x=600,y=500)

boton3quit = Button(ventana,text="X",bg='Red',command=ventana.quit)
boton3quit.place(x=780,y=0)

ventana.mainloop()
