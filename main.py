
from tkinter import *
from tkinter import ttk
from structure import App_structure
import json


class Main_class:
    def __init__(self, window, ruta):
        
        with open(ruta) as content:
            res = json.load(content)
            self.size  = res.get("size")
            self.title = res.get("title")

        self.wind = window
        self.wind.title(self.title)
        self.wind.geometry(self.size)
        labelLeft  = LabelFrame(self.wind, text="Ingresar texto:", pady=10, padx=15)
        labelLeft.grid(row=1, column=0)
        labelRight = LabelFrame(self.wind, text="Resultado del cambio:", pady=10, padx=15)
        labelRight.grid(row=1, column=1)
        self.struc = App_structure()
        self.struc.tex_area(labelLeft, labelRight)
        labelHead  = Label(self.wind, text="Data edit aplicación: v.1.0.0.1", justify=LEFT)
        labelHead.grid(row=3, column=0, columnspan=2)



if __name__ == "__main__":
    window = Tk()
    xRuta = "config_py.json"
    xCls  = Main_class(window, xRuta)
    window.mainloop()
