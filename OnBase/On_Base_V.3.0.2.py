# designed by Digtal Concept™
# Copyright © 05-11-2020 Bryan Urbina Guevara
# Programa que busca el numero de cajas de las remisiones para On_Base
#Version estable V.3.0.2
import os
import pandas as pd
import xlsxwriter


print("Buscando remisiones y numeros de cajas, Por favor espera...")
# Tipo de archivos que nos interesa encontrar
buscar = 'FL_CLARO_MASIVO_'
# Ruta donde encontraremos los archivos de la carpeta EDC_inventario 
path = 'C:\\Users\\logic\\Dropbox\\CLARO_2019\\INVENTARIO_EDC\\EDC_2021'
total = 0

# Con este bloque recorremos las carpetas para buscar los archivos con extencion xlsx (Excel)
"""
- root = Ruta de la carpeta
- dir = Nombre de la carpeta
- ficheros = Nombre del archivo
"""

# Con este bloque buscamos el tipo de archivo en la carpeta, lo pasamos a un Array para buscar en cada archivo el nombre de la remision
ruta = [] # Aqui se guardan lasrutas con el nombre de los archivos
for root, dir, ficheros in os.walk(path):
    for fichero in ficheros:
        if(buscar in fichero):
        	total += 1
        	ruta.extend([root+"\\"+fichero])

# path2 = 'C:\\Users\\Santiago\\Desktop\\BUSQUEDA_DATOS\\CLARO_MASIVO_FILES_LOGICSA_1.xlsx'
# Esta seran las coincidencia a buscar dentro de los archivos xlsx
bus = ['ARE070', 'REMISIONMOVILENERO', 'REMISIONMOVILENERO 2PARTE', 'REMISIONMULTIENERO', 'CM00146', 'CM00147', 'CM00148', 
'CM00149', 'MD 00398', 'MD 00399', 'MD 00402', 'MD 00404', 'DPL183', 'EDA0796', 'EDA0800', 'EDA0801', 'EDA0802', 'EDA0803',
 'Emarsa_02_2021_03', 'Emarsa_03_2021_03', 'Emarsa_04_2021_03', 'Emarsa_05_2021_03', 'CHONP20210101', 'DTH012021', 'GMSBOA012021', 
 'GMSMAT0121', 'GMSMGA1220', 'GMSMNGA0121', 'Gex.137', 'Gex.138', '12021', '3012021', '00401-INVERMOVIL', 'SMF_ENERO 2021', 'REMNISSI041', 
 'DPL0018', 'martha.sequeira-001-2021-0', 'MI0054', 'MI0055', 'MC0119', 'DRAMM05', 'AltaMulMill5', 'MTTECH_ENERO 2021', 'NESS 074', 'DC012021PP', 
 'RE024', 'REMISION No.1 ENERO', 'RISA0017', 'REM ENE 96 MULT', 'REM ENE 97 MULT', 'MOVILENERO21SEDICONISA1', 'M&MENERO2021', 'TJFCL0121M', 'TJFCL0121O', 
 'TJFM139', 'TJFM140', 'TL-04155', 'TL-04156', 'TL-04157', 'TL-04158', 'TL-04159', 'TL-04160', 'TL-04161', 
'TELPRONIC00229', 'MULTI.06', 'REM MOVIL 06', 'BL. 02-2021-0002', 'PZ 01.2021.002', 'PZ 01.2021.003', 'PZ. 01-2021-0001']

# Este for ayuda a leer los archivos xlsx encontrados
rem = [] #Aqui se guardan los nombres de las remisiones 
box = [] # Aqui se guardan los numero de las cajas
indice = []
contm = 0
for m in ruta:
	d = pd.read_excel(m, sheet_name = 'ALTAS NUEVAS')
	df = pd.DataFrame(data = d)
	cot_remision = 1 #Contadores para saber cuantan celdas bajo para encontrar el correcto
	cot_box = 1

	# Se crearan las listas vacias para guardar las remisiones y Numero de cajas que pertenece

	for f in bus: # Con este bloque se logra encontrar lo buscado de la remision
		for i in df['NOMBRE DE REMISION']:	
			cot_remision += 1
			if i == f:
				rem.extend([i])
				indice.extend([m])
				break
				#print("Remision agregada a la matriz")
		if i == f:
			for x in df['NUMERO DE CAJA']: # Con este otro se busca el numero de caja
				cot_box += 1
				if cot_box == cot_remision:
					box.extend([x])
		cot_box = 1
		cot_remision = 1
	if i == bus:
		break
	contm += 1

# incrustado con fines de pruebas para saber si funciona el codigo y la informacion la guarda en la matriz 
print("Proceso terminado con exito")
print("Cantidad de remisiones: ", len(bus))
print("cantidad de cajas: ", len(box))
print("Nombre remision: ", rem)
print("Numero de caja: ", box)
print("Archivos buscados: ", len(indice))
print("Salto rem: ", cot_remision)
print("Salto box: ", cot_box)
print("Paths rrecorridos: ",contm)
# Resultado esperado, todos los datos guardados los guarda en orden y correctamente

"""Este apartado para abajo es unicamente para mandar a crea otro documento que nos guarde la informacion buscada
NOTA: se hace de esta manera, ya que en pruebas anteriores, se comprobo que borra todo el contenido existente 
del libro en donde obtenemos la infromacin a buscar"""

r = pd.DataFrame(data = rem)
b = pd.DataFrame(data = box)
new = pd.DataFrame(b)
new.dropna(how = 'any', inplace =  True)

# Create a Pandas Excel writer using XlsxWriter as the engine.
out = 'boxes.xlsx'
writer = pd.ExcelWriter(out, engine='xlsxwriter')
r.to_excel(writer, sheet_name='Remisiones')
new.to_excel(writer, sheet_name='Cajas')
writer.save()

print("Busca el archivo: ", out , "en el escritorio o carpeta donde se ejecuto este codigo")