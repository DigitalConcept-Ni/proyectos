import pandas as pd
import json
from prueba import totales

path = 'C:/Users/logic/OneDrive/Escritorio/Asignacion Muestra Mayo_2021.xlsx'
d = pd.read_excel(path, sheet_name = 'Detalle')
df = pd.DataFrame(data = d)

list_problema = []


for p in df['PROBLEMA']:
	#if p == "CEDULA":
	list_problema.append(p)

# print(len(list_problema))


NOTIFICADOS = {

"CEDULA":["NO ESTA EN FISICO / ONBASE" , "FORMATO DE CEDULA DIFERENTE"],
	
"CONTRATO":["ESCANER INCOMPLETO","NO COINCIDE FISICO / ONBASE", "SIN FIRMA EN FISICO / ONBASE", "NO ESTA EN DIGITAL / FISICO", "COPIAS DE CONTRATOS FISICOS / DIGITAL"],
	
"FIRMA":["NO COINCIDE FISICO /  ONBASE","FIRMA ALTERADA","SIN FIRMA", "FIRMA DIFERENTE"],
	
"RECIBO BASICO":["NO COINCIDE FISICO / ONBASE"],
	
"COMPRABANTE DE INGRESOS":["NO COINCIDE FISICO / ONBASE"]

}

dicFinal = {}
CEDULA = {}
CONTRATO = {}
FIRMA = {}
RB = {} # RECIBO BASICO
CI = {} # COMPROBANTE DE INGRESOS

for clave,valor in NOTIFICADOS.items():
	# i = indice del valor encontrado
	# x = Valos dentro de la columna
	for i,x in enumerate(list_problema):
		#print(clave)
		if x == clave:
			# print("Problema: ", x)
			m = df.iloc[i]['COMENTARIO']
			#print("comentario: ", m)
			for v in valor:
				if m == v:
					# VALIDANDO PROBLEMAS CON CEDULAS
					if clave == "CEDULA":
						if v in CEDULA:
							CEDULA[v] += 1
						else:
							CEDULA[v] = 1
					# VALIDANDO PROBLEMAS CON CONTRATOS
					elif clave == "CONTRATO":
						if v in CONTRATO:
							CONTRATO[v] += 1
						else:
							CONTRATO[v] = 1
					# VALIDANDO PROBLEMAS CON FIRMA
					elif clave == "FIRMA":
						if v in FIRMA:
							FIRMA[v] += 1
						else:
							FIRMA[v] = 1
					# VALIDANDO PROBLEMAS CON RECIBO BASICO
					elif clave == "RECIBO BASICO":
						if v in RB:
							RB[v] += 1
						else:
							RB[v] = 1
					# VALIDANDO PROBLEMAS CON COMPRABANTE DE INGRESOS
					elif clave == "COMPRABANTE DE INGRESOS":
						if v in CI:
							CI[v] += 1
						else:
							CI[v] = 1

# print(dicFinal)
# r = totales(*CEDULA, *CONTRATO, *FIRMA, *RB, *CI)


# with open('file.txt', 'w') as file:
#      file.write(json.dumps(CONTRATO)) # use `json.loads` to do the reverse

# r = totales(CONTRATO)

print("\n")
# print("Total por incidencia: ", totalTipo)
# print("porcentaje total: ", porcentajeTotal)
print("Diccionario Contrato: ", CONTRATO)
print("Diccionario Cedula:  ", CEDULA)
print("Diccionario Firma:  ", FIRMA)
print("Diccionario Recibo Basico: ", RB)
print("Diccionario Comprobante de Iingresos: ", CI)

"""print(listProblemaFinal)
print(listComentarioFinal)"""


"""print("contador problema: ", contadorComentario, "\n")
print("contador comentario: ", contadorProblema) """