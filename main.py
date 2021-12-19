
from tkinter import *
from tkinter import ttk

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



if __name__ == "__main__":
    window = Tk()
    # xRuta = "config.py.json"
    xCls  = Main_class(window)
    
    window.mainloop()
