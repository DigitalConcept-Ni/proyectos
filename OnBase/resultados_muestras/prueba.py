
datos = {

"CONTRATO":  {'ESCANER INCOMPLETO': 23, 'NO COINCIDE FISICO / ONBASE': 5, 'NO ESTA EN DIGITAL / FISICO': 7},
"CEDULA":{'NO ESTA EN FISICO / ONBASE': 5},
"FIRMA":{'FIRMA ALTERADA': 9, 'SIN FIRMA': 3, 'FIRMA DIFERENTE': 4}
}

def totales(**kwargs):
	muestraTotal = 3749
	totalTipo = 0
	porcentajeTotal = 0
	dicFinal = []
	# print("prueba", kwargs)
	for clave, valor in kwargs.items():
		print("Tipo: ",clave)
		for c,v in kwargs[clave].items():
			# print("Incidencia: ", c, "cantidad: ", v)
			porcentaje = round((v/muestraTotal) * 100, 2)
			totalTipo += v
			porcentajeTotal += porcentaje
			# dicFinal.append([clave + ': ' + str(valor)+ ' ' + 'Porcentaje: ' + str(porcentaje)])
			print("Incidencia: ", c, "cantidad: ", v, "porcentaje: ", porcentaje, "\n")		

	print("\n")
	print("Total por incidencia: ", totalTipo)
	print("porcentaje total: ", round(porcentajeTotal, 2))
	print(dicFinal)

	#return dicFinal

fin = totales(**datos)

print(fin)


"""
NOTIFICADOS = {

"CEDULA":["NO ESTA EN FISICO / ONBASE" , "FORMATO DE CEDULA DIFERENTE"],
	
"CONTRATO":["ESCANER INCOMPLETO","NO COINCIDE FISICO / ONBASE", "SIN FIRMA EN FISICO / ONBASE", "NO ESTA EN DIGITAL / FISICO", "COPIAS DE CONTRATOS FISICOS / DIGITAL"],
	
"FIRMA":["NO COINCIDE FISICO /  ONBASE","FIRMA ALTERADA","SIN FIRMA", "FIRMA DIFERENTE"],
	
"RECIBO BASICO":["NO COINCIDE FISICO / ONBASE"],
	
"COMPRABANTE DE INGRESOS":["NO COINCIDE FISICO / ONBASE"]

}
with open('file.txt', 'w') as file:
     file.write(json.dumps(NOTIFICADOS)) # use `json.loads` to do the reverse"""
