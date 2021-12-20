from tkinter import *
from tkinter import ttk


class App_structure:
    def tex_area(self, object):
        self.lFrames = LabelFrame(object, text="Ingresar texto:")
        self.lFrames.pack()
        self.tarea = Text(self.lFrames, width=50, height=10)
        self.tarea.pack()
        self.sFrames = LabelFrame(object, text="Ingrese un caracter o palabra a buscar")
        self.sFrames.pack()
        self.input = Entry(self.sFrames)
        self.input.pack()
        self.Btn = Button(self.sFrames, text="Buscar", command=self.GetData)
        self.Btn.pack()



    def GetData(self):
        self.x_data  = self.input.get()
        self.x_tarea = self.tarea.get("1.0", "end")

        print(self.x_tarea.index(self.x_data))
                
        # self.labRes = Label(text=)
        
        # print(self.x_tarea)
        # print(self.x_data )

