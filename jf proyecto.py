from tkinter import*

ventana = Tk()
ventana.geometry("800x600")

menu=PhotoImage(file="Menu.gif")
juego=PhotoImage(file="Mario.gif")

def juego():
    global ventana1 
    ventana1=Toplevel()
    ventana1.geometry("800x600")
    
    ventana1.mainloop()



fotomenu=PhotoImage(file="Menu.gif")
lblImagen=Label(ventana,image=fotomenu).place(x=0,y=0)
#Ventana edición y botones:
ventana.config(bg="green")
ventana.title('Mario Bros')

#Cuadro de texto
Playername=Label(ventana,text="Player Name: ")
Playername.place(x=300,y=300)
variable_string = StringVar()
cajadetexto = Entry(ventana,textvariable=variable_string)
cajadetexto.place(x=400,y=300)


#Función comenzar (start) 
botonstart = Button(ventana,text="Start",bg='Brown',command=juego)
botonstart.place(x=400,y=350)

#Función un jugador                   
boton1player = Button(ventana,text="1 Player",bg='Red')
boton1player.place(x=600,y=500)


boton2players = Button(ventana,text="2 Players",bg='Green')
boton2players.place(x=200,y=500)

#Función cerrar (quit)

boton3quit = Button(ventana,text="X",bg='Red',command=quit)
boton3quit.place(x=780,y=0)
                           




