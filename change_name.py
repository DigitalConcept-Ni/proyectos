# Designe By Bryan Urbina Guevara For Logicsa 2021
# All rigth reserver Digital Concept 2021
# Program that change the name of documents

import os, time
import pandas as pd
# openpyxl

path = os.chdir('C:/Users/Santiago/Desktop/change_name')
archivo = 'C:/Users/Santiago/Desktop/DATA.xlsx' # Nombre del archivo de nombres
contador = 0 # Unicamente con la funcion de contar la cantidad de archivos
name_file = [] # Save all file name
nombre_anterior = []
new = []

def generador():
	d = pd.read_excel(archivo, sheet_name='Hoja1')
	df = pd.DataFrame(data=d)
	documents = []

	for i in df['NOMBRE DOCUMENTO']:
		yield i

r = generador()

# Separa los archivos pdf con el programa '.py'
for f in os.listdir(path):
	name, typeFile = os.path.splitext(f)
	if typeFile == '.py':
		continue
	else:
		name_file.append(name + typeFile)
		nombre_anterior.append(name + typeFile)
		contador += 1 # Cuenta la cantidad de archivos ejecutados

name_file.sort(key=os.path.getctime)

# here chane name this file's
for file in name_file:
	name = file.replace(file,next(r))
	new_name = name + '.pdf'
	new.append(new_name)
	os.replace(file,new_name)


for i in new:
	# print( "Nombre: ", i ,"\nFecha: "," {}".format(time.ctime(os.path.getctime(i))))
	# print('Nombre anterior: ', i, '\nNumero nombre: ',next(data))
	print(i)

print('cantidad archivo: ', contador)