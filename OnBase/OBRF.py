from tkinter import * 
from tkinter import filedialog

raiz = Tk()
raiz.geometry('250x250')

# boton1 = tk.Button(raiz, text = 'Boton1')
# boton2 = tk.Button(raiz, text = 'Boton2')
# boton3 = tk.Button(raiz, text = 'Boton3')

# boton1.grid(row = 0, column =0)
# boton2.grid(row = 1, column =1)
# boton3.grid(row = 2, column =2)


etiqueta = Label(raiz, text='OBRF')
etiqueta.grid(row = 1, column =2)

TiposdeArchivos = ('Archivos Excel', '*.xlsx'),('Archvios PDF', '*.pdf')

def abriArchivo():
	archivo = filedialog.askopenfile(title = 'Abrir documento', filetypes = TiposdeArchivos)

	try:
	    print(archivo.name)		
	except Exception as e:
		return print('No seleccionastes Un archivo')
	return archivo.name


btn_abrirArchivo = Button(raiz, text = 'Abrir Documento', command = abriArchivo)
btn_abrirArchivo.grid(row = 2, column = 3)

message = Label(raiz, text= '')
message.grid(row = 3, column = 2, columnspan = 2, sticky = W + E )
message['text'] = '{}'.format(abriArchivo.name)



raiz.mainloop()