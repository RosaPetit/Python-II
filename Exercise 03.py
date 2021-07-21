'''Programa 3(utilizacion del if,elif y else)'''

# Utilicemos el if

a= float( input('\n Introdusca un numero: \n '))


if (a<100) & (a>0):
	print(a, "\n a es menos que 100 y mayor que cero\n ")

elif a>100:
	print(a, "\n a es mayor que 100\n ")

elif a<-100:
	print(a, "\n a es menor que -100\n")

else:
	print(a, "\n a es menor que cero, pero mayor que -100 \n ")




