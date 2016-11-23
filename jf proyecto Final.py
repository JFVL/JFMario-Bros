from tkinter import*

ventana = Tk()
ventana.geometry("800x600")
#Imagenes
menu=PhotoImage(file="Menu.gif")
juego=PhotoImage(file="Mario.gif")
mario1=PhotoImage(file="Mario sprites(parado).png")
mario2=PhotoImage(file="Mario sprites(paso).png")
posx=100
posy=400
#Juego

def juego(event):
    global ventana1,canvas1,mario2,mario1,tec
    tec=repr(event.chat)
    ventana1=Toplevel()
    ventana1.geometry("800x600")
    canvas1=Canvas(ventana1, width=800, height=600)
    juego=PhotoImage(file="Mario.gif")
    canvas1.create_image(0,0,anchor=NW,image=juego)
    mario1=PhotoImage(file="Mario sprites(parado).png")
    canvas1.create_image(0,0,anchor=NW,image=mario1)

    x=int(canvas1.coords(mario2)[0])
    y=int(canvas1.coords(mario2)[1])
    
# d o D, para moverse al lado derecho.
    if(tec=="'d'")or(tec=="'D'"):
        mario1=canvas1.coords(mario2)
        ventana1.delete(mario2)
        mario2=canvas1.create_image(x,y,image=mariodere)
        estadomario="derecha"
        canvas1.move(mario2,10,0)
    if(canvas1.coords(mario2)[0]>1280):
       canvas1.coords(mario2,10,int(canvas1.coords(mario2)[1]))
    if(canvas1.coords(mario2)[1]==490 and (canvas1.coords(mario2)[0]>=480 and canvas1.coords(mario2)[0]<=799)):
       caida()
    if(canvas1.coords(mario2)[1]==360 and (canvas1.coords(mario2)[0]>=160 and canvas1.coords(mario2)[0]<=320)):
       caida()
    if(canvas1.coords(mario2)[1]==360 and (canvas1.coords(mario2)[0]>=963 and canvas1.coords(mario2)[0]<=1120)):
       caida()
    if(canvas1.coords(mario2)[1]==180 and (canvas1.coords(mario2)[0]>=561 and canvas1.coords(mario2)[0]<=720)):
       caida()
    if(canvas1.coords(mario2)[0]==canvas1.coords(enemigos1)[0]) and (canvas1.coords(mario2))[1] == canvas1.coords(mario2)[1]==canvas1.coords(enemigo1)[1]:
       canvas1.delete(mario2)
       respawn()
# a o A, para moverse al lado izqueirdo.
    if((tec=="'a'")or(tec=="'A'")):
        p1=canvas1.coords(mario2)
        canvas1.delete(mario2)
        mario2=canvas1.create_image(x,y,image=marioizq)
        estadomario="izquierda"
    canvas1.move(mario2,-10,0)
    if(canvas1.coords(mario2)[0]<0):
       canvas1.coords(mario2,1270,int(canvas1.coords(mario2)[1]))
    if(canvas1.coords(mario2)[1]==490 and (canvas1.coords(mario2)[0]>=480 and canvas1.coords(mario2)[0]<=799)):
       caida()
    if(canvas1.coords(mario2)[1]==360 and (canvas1.coords(mario2)[0]>=160 and canvas1.coords(mario2)[0]<=320)):
       caida()
    if(canvas1.coords(mario2)[1]==360 and (canvas1.coords(mario2)[0]>=963 and canvas1.coords(mario2)[0]<=1120)):
       caida()
    if(canvas1.coords(mario2)[1]==180 and (canvas1.coords(mario2)[0]>=561 and canvas1.coords(mario2)[0]<=720)):
       caida()
    if(canvas1.coords(mario2)[0]==canvas1.coords(enemigos1)[0]) and (canvas1.coords(mario2))[1] == canvas1.coords(mario2)[1]==canvas1.coords(enemigo1)[1]:
       canvas1.delete(mario2)
       respawn()
       
    
    canvas1.pack()
    canvas1.focus_set()
    canvas1.bind('<key>',juego)
    ventana1.mainloop()

#Menu

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
boton1player = Button(ventana,text="1 Player",bg='Red',command=juego)
boton1player.place(x=600,y=500)


boton2players = Button(ventana,text="2 Players",bg='Green')
boton2players.place(x=200,y=500)

#Función cerrar (quit)

boton3quit = Button(ventana,text="X",bg='Red',command=quit)
boton3quit.place(x=780,y=0)


juego()
ventana.resizable(0,0)
ventana.mainloop()





