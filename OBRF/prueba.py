import pandas as pd

def Remisiones():
	path = 'C:\\Users\\logic\\OneDrive\\Escritorio\\Asignacion Muestra Abril_2021.xlsx'
	d = pd.read_excel(path, sheet_name = 'Hoja1')
	df = pd.DataFrame(data = d)
	remision = []	
	for i in df['Remision']:
		remision.extend([i])
	# print(remision)
	return remision

r = Remisiones()

print(r)
print("cantidad de remisiones", len(r))