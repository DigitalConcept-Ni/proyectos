import pandas as pd



path = 'C:/Users/logic/OneDrive/Escritorio/Asignacion Muestra Mayo_2021.xlsx'
d = pd.read_excel(path, sheet_name = 'Detalle')
df = pd.DataFrame(data = d)

list_problema = []
list_comentario = []	

#contadorProblema = 0
#contadorComentario = 0

print(df['PROBLEMA'])

"""for p in df['PROBLEMA']:
	if p == "CEDULA":
		list_problema.extend([p])		
		for c in df['COMENTARIO']:
			if c == 'FORMATO DE CEDULA DIFERENTE':
				contadorComentario += 1

print("contador problema: ", contadorComentario, "\n")
print("contador comentario: ", contadorProblema) """

