
datos = {

"CONTRATO":{'ESCANER INCOMPLETO': 20, 'NO COINCIDE FISICO / ONBASE': 1, 'SIN FIRMA EN FISICO / ONBASE': 3, 'NO ESTA EN DIGITAL / FISICO': 5},
"FIRMA":{"NO COINCIDE FISICO /  ONBASE": 10, "FIRMA ALTERADA": 20,"SIN FIRMA": 25, "FIRMA DIFERENTE": 45}
}

def totales(*kwargs):
	muestraTotal = 3749
	totalTipo = 0
	porcentajeTotal = 0
	dicFinal = []
	print("prueba", kwargs)
	for clave, valor in kwargs.items():
		break
		print("clave valor",clave)
		for c, v in kwargs[clave].items():
			print(c, v)
			porcentaje = round((v/muestraTotal) * 100, 2)
			totalTipo += v
			porcentajeTotal += porcentaje
			# dicFinal.append([clave + ': ' + str(valor)+ ' ' + 'Porcentaje: ' + str(porcentaje)])
			print("porcentaje: ", porcentaje, "\n")
		

	print("\n")
	print("Total por incidencia: ", totalTipo)
	print("porcentaje total: ", round(porcentajeTotal, 2))
	print(dicFinal)

	#return dicFinal

# fin = totales(**datos)

# print(fin)


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
