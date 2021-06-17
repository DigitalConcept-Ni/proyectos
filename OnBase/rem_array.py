# Programa para agregar los nombres de las remisiones.

import pandas as pd

path = 

d = pd.read_excel(path, sheet_name = 'Hoja1')
df = pd.DataFrame(data = d)

remision = []	

for i in df['Remision']:
	remision.extend([i])
print(remision)
print("total remisiones: ", len(remision))