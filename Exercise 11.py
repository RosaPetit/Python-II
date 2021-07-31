'''Crea una chiquita ventana con un mensaje'''

from tkinter import *

#Creo la ventana prinsipal

raiz=Tk()

def funcion():
	print("Me caes bien")

def funcion2():
	print("Me caes mal")

#creo el lienzo

w=400 #ancho del lienzo
h=300 #altura del lienzo

lienzo= Canvas(raiz, width= w, height=h)

lienzo.pack()

botoncitoI= Button(text="No te gusta el rosado", fg="red", command=  funcion2)
botoncitoI.pack(side=LEFT)

botoncitoD= Button(text="Te gusta el rosado",fg="blue", command= funcion)
botoncitoD.pack(side=RIGHT)

#botoncitoM= Button(text="No me importa", command= quit)
#botoncitoM.pack(side=HALF)

#dibujo de una elipse

x0=120
y0=111
x1=180
y1=150

lienzo.create_oval(x0,y0,x1,y1, fill="pink", tag="nombre")


raiz.mainloop()
