import os


buscar = 'FL_CLARO_MASIVO_'
# Ruta donde encontraremos los archivos de la carpeta EDC_inventario 
path = 'C:\\Users\\logic\\Dropbox\\CLARO_2019\\INVENTARIO_EDC\\EDC_2021'

# Con este bloque recorremos las carpetas para buscar los archivos con extencion xlsx (Excel)
"""
- root = Ruta de la carpeta
- dir = Nombre de la carpeta
- ficheros = Nombre del archivo
"""

# Con este bloque buscamos el tipo de archivo en la carpeta, lo pasamos a un Array para buscar en cada archivo el nombre de la remision
ruta = [] # Aqui se guardan lasrutas con el nombre de los archivos

def BusquedaArchivo():
	total = 0

	for root, dir, ficheros in os.walk(path):
	    for fichero in ficheros:
	        if(buscar in fichero):
	        	total += 1
	        	ruta.extend([root+"\\"+fichero])
	        	#yield ruta
	return ruta
