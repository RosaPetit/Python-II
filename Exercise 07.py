'''Programa 6 '''

a=range(0,501)

for i in a:
	resto = i%3
	print(i,resto)

	if resto==0:
		print("Es multiplo de tres")
	else:
		print("No es multiplo de tres")
