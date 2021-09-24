import re
import string
alfabeto = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','Ñ','O','P','Q','R','S','T','U','V','W','X','Y','Z']
def nuevaClave(clave,longitud):
	key = ""
	i=0
	j=0
	for i in range (longitud):
		if i>0 and (i%len(clave)==0):
			j=0
		key = key+clave[j]
		j=j+1
	return key

def getIndice(letra):
	index=alfabeto.index(letra)
	return index
def descifrarAutoclave(cifrado,clave):
	texto=""
	key = nuevaClave(clave.upper(),len(cifrado))
	m=0
	j=0
	n=0
	for i in cifrado:
		if n<len(clave):
			m=((getIndice(i))+(27-getIndice(clave[n])))%(27)
			n=n+1
			texto=texto+alfabeto[m]
		else:
	   		m=((getIndice(i))+(27-getIndice(texto[j])))%27
		   	print(m)
		   	j=j+1
		   	texto = texto+alfabeto[m]
	return texto
def main():
	print("*****************CIFRADO*********************************")
	clave="UNODELOSMASGRANDESCRIPTOGRAFOS"
	f=open("descifrar2.txt",'r')
	texto =f.read()
	cifrado=descifrarAutoclave(texto,clave)
	fs=open("pruebasalidadescifrado2.txt",'a')
	fs.write(cifrado)
	fs.close()
	
main()
