from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from Search import BusquedaCajaRemision
import time
from threading import Thread

class Onbase():
    archivo = ""

    def __init__(self, window):
        #archivo = ""
        self.wind = window
        self.wind.title('OBRF')
        self.wind.configure(bg = "#041f3a")

        # Creating a frame from control the form
        frame = LabelFrame(self.wind, text = "  WELCOME TO ONBASE BOX AND REFERRALS FINDER  ",fg = "#FDFEFE", font=("Dubai Medium", 12), bg = "#041f3a")
        frame.grid(row = 0, column = 0, columnspan = 2, pady = 20, padx = 100)

        # tag principal
        Title = Label(frame, text = 'Seleccionar Archivo:  ',fg = "#FDFEFE",font=("Dubai", 12), bg = "#041f3a", relief=FLAT).grid(row = 1, column = 0, pady = 20)
        ttk.Button(frame,text = 'Abrir',command = self.AbrirArchivo).grid(row = 1, column = 2)

        #button for star finder
        iniciar = ttk.Button(frame,text = 'Iniciar Busqueda',command = self.button)
        iniciar.grid(row = 1,column = 3, columnspan = 2,padx = 15, sticky = W + E)

        # messages build
        self.message = Label(text = 'Archivo: ',fg = "#FDFEFE",bg = "#041f3a",font=("Dubai", 12), padx = 15)
        self.message.grid(row = 3, column = 0,columnspan = 2, sticky = W)

        self.message01 = Label(text = '',fg = "#f7931e",bg = "#041f3a",font=("Dubai", 13), padx = 15)
        self.message01.grid(row = 5, column = 0,columnspan = 2, sticky = W + E)


        self.message1 = Label(text = '',fg = "#f7931e",bg = "#041f3a",font=("Dubai", 14), padx = 15)
        self.message1.grid(row = 4, column = 0,columnspan = 2, sticky = W + E)

        self.message2 = Label(text = 'Cantidad de Remisiones: ',fg = "#FDFEFE",bg = "#041f3a",font=("Dubai", 12), padx = 15)
        self.message2.grid(row = 6, column = 0,columnspan = 2, sticky = W)

        self.message3 = Label(text = 'Cantidad de Cajas: ',fg = "#FDFEFE",bg = "#041f3a",font=("Dubai", 12), padx = 15)
        self.message3.grid(row = 7, column = 0,columnspan = 2, sticky = W)

        self.message4 = Label(text = 'Cantidad de Archivos Buscados: ',fg = "#FDFEFE",bg = "#041f3a",font=("Dubai", 12), padx = 15)
        self.message4.grid(row = 8, column = 0,columnspan = 2, sticky = W)

        self.message5 = Label(text = 'Cantidad de Archivos Excel Recorridos: ',fg = "#FDFEFE",bg = "#041f3a",font=("Dubai", 12), padx = 15)
        self.message5.grid(row = 9, column = 0,columnspan = 2, sticky = W)

        self.message6 = Label(text = '',fg = "#FDFEFE",bg = "#041f3a",font=("Dubai", 12), padx = 15)
        self.message6.grid(row =10, column = 0,columnspan = 2, sticky = W)

        self.message7 = Label(text = 'Designed By Bryan Urbina © Digital Concept 2021',fg = "#f7931e",bg = "#041f3a",font=("Dubai", 10))
        self.message7.grid(row =11, column = 0,columnspan = 2, sticky = W + E)

        # ------------------------------------------------------

    def AbrirArchivo(self):
        nameFile = filedialog.askopenfilename(title = "Abrir")
        self.archivo = nameFile
        if self.archivo == "":
            self.message1['text'] = '---- NO HA SELECCIONADO NINGUN ARCHIVO ----'
            #self.iniciar['state'] = ENABLED
        else:
            self.message['text'] += '{}'.format(self.archivo)
            self.message['fg'] = '#f7931e'
            self.message1['text'] = '=== Tiempo estimado para la busqueda "3 min" Aprox ==='
            return self.archivo

    def Arranque(self):
        if self.archivo == "":
            self.message1['text'] = '---- NO HA SELECCIONADO NINGUN ARCHIVO ----'
        else:
            self.message01['text'] = '---- INICIANDO ----'
            r = BusquedaCajaRemision(self.archivo)
            self.message2['text'] += '{}'.format(r[0])
            self.message3['text'] += '{}'.format(r[1])
            self.message4['text'] += '{}'.format(r[2])
            self.message5['text'] += '{}'.format(r[3])
            self.message6['text'] += '{}'.format(r[4])

    def button(self):
        Thread(target = self.Arranque).start()


if __name__ == '__main__':
    window = Tk()
    application = Onbase(window)
    window.mainloop() 