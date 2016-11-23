from tkinter import*
def movimiento(event):
    global c,mario2,estadomario,tec,boo,enemigo1
    x=int(c.coords(mario2)[0])
    y=int(c.coords(mario2)[1])
# d o D, para moverse al lado derecho.
    if(tec=="'d'")or(tec=="'D'"):
    p1=c.coords(mario2)
    c.delete(mario2)
    mario2=c.create_image(x,y,image=mariodere)
    estadomario="derecha"
    c.move(mario2,10,0)
    if(c.coords(mario2)[0]>1280):
       c.coords(mario2,10,int(c.coords(mario2)[1]))
    if(c.coords(mario2)[1]==490 and (c.coords(mario2)[0]>=480 and c.coords(mario2)[0]<=799)):
       caida()
    if(c.coords(mario2)[1]==360 and (c.coords(mario2)[0]>=160 and c.coords(mario2)[0]<=320)):
       caida()
    if(c.coords(mario2)[1]==360 and (c.coords(mario2)[0]>=963 and c.coords(mario2)[0]<=1120)):
       caida()
    if(c.coords(mario2)[1]==180 and (c.coords(mario2)[0]>=561 and c.coords(mario2)[0]<=720)):
       caida()
    if(c.coords(mario2)[0]==c.coords(enemigos1)[0]) and (c.coords(mario2))[1] == c.coords(mario2)[1]==c.coords(enemigo1)[1]:
       c.delete(mario2)
       respawn()
# a o A, para moverse al lado izqueirdo.
    if((tec=="'a'")or(tec=="'A'")):
    p1=c.coords(mario2)
    c.delete(mario2)
    mario2=c.create_image(x,y,image=marioizq)
    estadomario="izquierda"
    c.move(mario2,-10,0)
    if(c.coords(mario2)[0]<0):
       c.coords(mario2,1270,int(c.coords(mario2)[1]))
    if(c.coords(mario2)[1]==490 and (c.coords(mario2)[0]>=480 and c.coords(mario2)[0]<=799)):
       caida()
    if(c.coords(mario2)[1]==360 and (c.coords(mario2)[0]>=160 and c.coords(mario2)[0]<=320)):
       caida()
    if(c.coords(mario2)[1]==360 and (c.coords(mario2)[0]>=963 and c.coords(mario2)[0]<=1120)):
       caida()
    if(c.coords(mario2)[1]==180 and (c.coords(mario2)[0]>=561 and c.coords(mario2)[0]<=720)):
       caida()
    if(c.coords(mario2)[0]==c.coords(enemigos1)[0]) and (c.coords(mario2))[1] == c.coords(mario2)[1]==c.coords(enemigo1)[1]:
       c.delete(mario2)
       respawn()
       
