from tkinter import *
from tkinter import ttk
from typing import ValuesView


class App_structure:
    def tex_area(self, objectA, objectB, labBG, colorTextLabel):
        self.labBG = labBG
        #-----------------------------------------------------------------------------------------------------
        self.lFrames = LabelFrame(objectA, bg=labBG, fg=colorTextLabel)
        self.lFrames.pack()
        #-----------------------------------------------------------------------------------------------------
        self.tareaA = Text(self.lFrames, width=50, height=10)
        self.tareaA.pack()
        #-----------------------------------------------------------------------------------------------------
        self.sFrames = LabelFrame(objectA, text="Ingrese un caracter o palabra a buscar", bg=labBG, fg=colorTextLabel)
        self.sFrames.pack()
        #-----------------------------------------------------------------------------------------------------
        self.lab_char = Label(self.sFrames, bg=labBG, fg=colorTextLabel, text="Caracter a buscar:")
        self.lab_char.pack(side=LEFT)
        #-----------------------------------------------------------------------------------------------------        
        self.inputB = Entry(self.sFrames)
        self.inputB.pack(side=LEFT)
        #-----------------------------------------------------------------------------------------------------       
        self.lab_char = Label(self.sFrames, bg=labBG, fg=colorTextLabel, text="Caracter a reemplazar:")
        self.lab_char.pack(side=LEFT)
        #-----------------------------------------------------------------------------------------------------        
        self.input = Entry(self.sFrames)
        self.input.pack(side=LEFT)
        #-----------------------------------------------------------------------------------------------------       
        self.Btn = Button(self.sFrames, text="Buscar", command=lambda: self.GetData(objectA))
        self.Btn.pack(side=BOTTOM)
        #-----------------------------------------------------------------------------------------------------        
        self.rightFrames = LabelFrame(objectB)
        self.rightFrames.pack()
        #-----------------------------------------------------------------------------------------------------        
        self.tareaB = Text(self.rightFrames, bg="gray", fg="black", 
                           width=50, height=14)
        self.tareaB.insert("1.0", "Esperando data...")
        self.tareaB.pack()
        #-----------------------------------------------------------------------------------------------------        
        # self.labRes = Label(objectA, fg="green", bg=self.labBG,
        #                     padx=5, pady=5, text= "C. Ingresados: " + self.c_data)        
        # self.labRes.pack(side=RIGHT)
        #-----------------------------------------------------------------------------------------------------        


    def GetData(self, objectA):
        #caracter a reemplazar
        self.x_data     = self.input.get()
        #caracter a buscar para cambiar
        self.changeData = self.inputB.get()
        print(self.changeData)
        self.x_tarea = self.tareaA.get("1.0", "end")
        # m = self.x_tarea.index(self.x_data)
        
        self.rep_cadena = self.x_tarea.replace(self.changeData, self.x_data)
        print(self.rep_cadena)

        self.tareaB.delete("1.0", END)
        self.tareaB.insert("1.0", self.rep_cadena)
        # self.x_tarea
        
        
        # self.c_data = str(self.Longitud(self.x_tarea))

        
        # self.labRes = Label(self.sFrames, fg="green", bg="#D6D6D6",
        #                     padx=5, pady=5, text= "Número de caracteres ingresados: " + self.c_data)  
        
        # self.labRes.pack()
        
        
        
        
    def Longitud( self, data_analizar ):
        x   = list( data_analizar )
        s_x = len ( x )
        return s_x


