
from tkinter import *
from tkinter import ttk
from structure import App_structure
import json


class Main_class:
    def __init__(self, window):
        
        # with open(src) as content:
        #     res = json.load(content)
        #     self.size = res.get("title")
        #     self.title = res.get("size")

        self.wind = window
        self.wind.title("App search text")
        self.wind.geometry("600x350")
        
        
        self.struc = App_structure()
        self.struc.tex_area(self.wind)



if __name__ == "__main__":
    window = Tk()
    # xRuta = "config.py.json"
    xCls  = Main_class(window)
    
    window.mainloop()
