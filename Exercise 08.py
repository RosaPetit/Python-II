'''Programa 7 '''
#Primer ciclo
for n in range(2,20):
	for i in range(2,n):
#ciclo anidado
		if(n%i)==0:
			print(n,'es igual a', i,'*',n/i)
#break rompe el ciclo anidado
			break
# el else esta como una alternativa	
	else:
		print(n,"el numero es primo")
