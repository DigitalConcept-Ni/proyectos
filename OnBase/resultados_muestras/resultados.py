import pandas as pd

path = 'C:/Users/logic/OneDrive/Escritorio/Asignacion Muestra Mayo_2021.xlsx'
d = pd.read_excel(path, sheet_name = 'Detalle')
df = pd.DataFrame(data = d)

list_problema = []


for p in df['PROBLEMA']:
	#if p == "CEDULA":
	list_problema.append(p)

#listProblemaFinal = []
#listComentarioFinal = []

Problemas = ['CEDULA','CONTRATO','FIRMA','RECIBO BASICO','COMPRABANTE DE INGRESOS']

"""CEDULA= ["NO ESTA EN FISICO / ONBASE" , "FORMATO DE CEDULA DIFERENTE"]
	
CONTRATO = ["NO COINCIDE FISICO / ONBASE", "SIN FIRMA EN FISICO / ONBASE", "NO ESTA EN DIGITAL / FISICO", "COPIAS DE CONTRATOS FISICOS / DIGITAL"]
	
FIRMA = ["NO COINCIDE FISICO /  ONBASE","FIRMA ALTERADA","SIN FIRMA"]
	
RECIBO BASICO = ["NO COINCIDE FISICO / ONBASE"]
	
COMPRABANTE DE INGRESOS = ["NO COINCIDE FISICO / ONBASE"]"""


dicFinal = {}

print("Diccionario:", dicFinal)

CEDULA = {}
CONTRATO = {}
RB = {}
CI = {}

for p in Problemas:
	cont = 0
	# i = indice del valor encontrado
	# x = Valos dentro de la columna
	for i,x in enumerate(list_problema):
		if x == p:
			m = df.iloc[i]['COMENTARIO']
			cont += 1
			if p == 'FIRMA':
				CEDULA[m] = cont
			#listProblemaFinal.append(x)
			#listComentarioFinal.append(m)
			#print(i, " | ")
			#print(m)
	break

print("Diccionario con valores: ", CEDULA)

"""print(listProblemaFinal)
print(listComentarioFinal)"""


"""print("contador problema: ", contadorComentario, "\n")
print("contador comentario: ", contadorProblema) """

