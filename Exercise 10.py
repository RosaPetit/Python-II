'''Crea una chiquita ventana con un mensaje'''

from tkinter import *

#Creo la ventana prinsipal

raiz=Tk()

def funcion():
	print("Me voy pal monte")
	
#Boton que va a la izquierda
	
botoncitoI= Button(text="QUIT", fg="red", command= quit)
botoncitoI.pack(side=LEFT)

#para que el boton se vea se utiliza pack

#Boton que va ala derecha

botoncitoD= Button(text="a dodne vas", command= funcion)
botoncitoD.pack(side=RIGHT)

raiz.mainloop()

