# Programa para agregar los nombres de las remisiones.

import pandas as pd


def Remisiones(path):
	#path = 'C:\\Users\\logic\\OneDrive\\Escritorio\\Asignacion Muestra Abril_2021.xlsx'
	d = pd.read_excel(path, sheet_name = 'Hoja1')
	df = pd.DataFrame(data = d)
	remision = []	
	for i in df['Remision']:
		remision.extend([i])
	# print(remision)
	return remision

	#print("total remisiones: ", len(remision))

#rem = 'C:\\Users\\logic\\OneDrive\\Escritorio\\Asignacion Muestra Abril_2021.xlsx'

