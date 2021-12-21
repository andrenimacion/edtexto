from tkinter import *
from tkinter import ttk
from structure import App_structure
import json


class Main_class:
    def __init__(self, window, ruta):
        
        with open(ruta) as content:
            res = json.load(content)
            self.backGroundApp  = res.get("bacground-App")
            self.labelBG        = res.get("label-bg")
            self.textColLab     = res.get("text-label-color")

        self.wind = window
        self.wind.title("WorkTomic")
        self.wind.geometry("997x300")
        self.wind.config(background=self.backGroundApp)
        labelLeft  = LabelFrame(self.wind, text="Ingresar texto:",
                                pady=10, padx=15, bg=self.labelBG, fg=self.textColLab)
        labelLeft.grid(row=1, column=0)
        labelRight = LabelFrame(self.wind, text="Resultado del cambio:", 
                                pady=10, padx=15, bg=self.labelBG, fg=self.textColLab)
        labelRight.grid(row=1, column=1)
        self.struc = App_structure()
        self.struc.tex_area(labelLeft, labelRight, self.labelBG, self.textColLab)
        labelHead  = Label(self.wind, text="Data edit aplicación: v.1.0.0.1", justify=LEFT,
                           bg=self.labelBG, fg=self.textColLab)
        labelHead.grid(row=3, column=0, columnspan=2)


if __name__ == "__main__":
    window = Tk()
    xRuta = "config_py.json"
    xCls  = Main_class(window, xRuta)
    window.mainloop()
