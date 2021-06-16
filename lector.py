import pandas as pd
# openpyxl


def archivo():
	archivo = 'C:/Users/Santiago/Desktop/DATA.xlsx'
	d = pd.read_excel(archivo, sheet_name='Hoja1')
	df = pd.DataFrame(data=d)
	documents = []

	# for i in df['NOMBRE DOCUMENTO']:
	# 	# documents.append(i)
	# 	yield i
	return print(df['NOMBRE_DOCUMENTO'])


# r = archivo()
archivo()

# print(next(r))
# print(next(r))
