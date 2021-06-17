# Designed by Digtal Concept™
# Copyright © 05-11-2020 Bryan Urbina Guevara
# Programa que busca el numero de cajas de las remisiones para On_Base
#Version estable V.3.0.2
import os
import pandas as pd
import xlsxwriter
from archivoCarpeta import BusquedaArchivo
from referralFinder import Remisiones


def BusquedaCajaRemision(path):
	ubicacionArchivo = BusquedaArchivo() # Ubicacion de los archivos
	nombreRemisiones = Remisiones(path) #Nombre de las remisiones
	# Este for ayuda a leer los archivos xlsx encontrados
	rem = [] #Aqui se guardan los nombres de las remisiones 
	box = [] # Aqui se guardan los numero de las cajas
	indice = []
	contm = 0 # Contador de paths
	
	for m in ubicacionArchivo:
		d = pd.read_excel(m, sheet_name = 'ALTAS NUEVAS')
		df = pd.DataFrame(data = d)
		cot_remision = 1 #Contadores para saber cuantan celdas bajo para encontrar el correcto
		cot_box = 1

		# Se crearan las listas vacias para guardar las remisiones y Numero de cajas que pertenece

		for f in nombreRemisiones: # Con este bloque se logra encontrar lo buscado de la remision
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
		if i == nombreRemisiones:
			break
		contm += 1

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

	#print("Busca el archivo: ", out , "en el escritorio o carpeta donde se ejecuto este codigo")

# incrustado con fines de pruebas para saber si funciona el codigo y la informacion la guarda en la matriz 
	# print("Proceso terminado con exito")
	# print("Cantidad de remisiones: ", len(nombreRemisiones))
	# print("cantidad de cajas: ", len(box))
	# print("Nombre remision: ", rem)
	# print("Numero de caja: ", box)
	# print("Archivos buscados: ", len(indice))
	# print("Paths rrecorridos: ",contm)
	final = "Busca el archivo:", out , " en el escritorio"
	result = [len(nombreRemisiones), len(box), len(indice), contm, final]
	return result
# Resultado esperado, todos los datos guardados los guarda en orden y correctamente


