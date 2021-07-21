'' 'Programa para leer archivo de notas'''

#nombre= input("Introdusca el nombre del archivo que quiere abrir:")

try:
	lectura=open("Archivo", "r")
#"nombre" no esta en comillas en el programa debido a que es una variable, no una cadenaa de caracteres

except IOError:
	#El excepe error es para saber que hay un error en el programa 
	print("Sr.Usuario: el archivo de datos no se puedo abrir")
	exit()

#Para que el programa lea la cantidad de alumnos por si solo agregamos un contador "cont=0"
cont=0

suma1=0
suma2=0
suma3=0
suma4=0

for ren in lectura:
	cont+=1
	lis=ren.split()

#El split es para convertir las notas en una lista
	promedio=(float(lis[1])+float(lis[2])+float(lis[3])+float(lis[4]))/4

#suma=suma+lis[0]:
	suma1+=float(lis[1])
	suma2+=float(lis[2])
	suma3+=float(lis[3])
	suma4+=float(lis[4])
	#print("El promedio del alumno", lis[0],"es", round(promedio))


promedio1=suma1/cont
promedio2=suma2/cont
promedio3=suma3/cont
promedio4=suma4/cont

print("El promedio de la primera columna es:",promedio1)
print("El promedio de la segunda columna es;", promedio2)
print("El promedio de la tercera columna es:",promedio3)
print("El promedio de la cuarta columna es;", promedio4)


