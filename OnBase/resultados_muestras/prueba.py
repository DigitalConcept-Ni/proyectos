

CONTRATO = {'ESCANER INCOMPLETO': 20, 'NO COINCIDE FISICO / ONBASE': 1, 'SIN FIRMA EN FISICO / ONBASE': 3, 'NO ESTA EN DIGITAL / FISICO': 5}

muestraTotal = 3749
totalTipo = 0
porcentajeTotal = 0
for clave, valor in CONTRATO.items():
	print(clave, valor)
	porcentaje = round((valor/muestraTotal) * 100, 2)
	totalTipo += valor
	porcentajeTotal += porcentaje 
	print("porcentaje: ", porcentaje, "\n")

print("\n")
print("Total por incidencia: ", totalTipo)
print("porcentaje total: ", porcentajeTotal)
	
