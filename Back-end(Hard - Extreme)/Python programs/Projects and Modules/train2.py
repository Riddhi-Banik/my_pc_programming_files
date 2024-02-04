import tkinter as tk
from tkinter import ttk
from tkinter import *
import RDHI_AdvCustomModule

anc = 0





class TK:
    def __init__(self):
        self._master_name = None
        self._main = tk.Tk()
        self._main.title("Making variablese")
        self._main.geometry("800x800")

        self._btn = tk.Button(text=f"Click to add", font=("Arial", 22), bg="cyan", command=self.adder)
        self._btn.pack()

        self._btn = tk.Button(text=f"Click to modify 9 to 7", font=("Arial", 22), bg="cyan", command=self.cgc)
        self._btn.pack()

        self._model = tk.Label(text="A", font=("Arial", 22))
        #self._model.pack()



        self._main.mainloop()
    def cgc(self):
        self._model9.config(text="7")
    def adder(self):
        global anc
        anc += 1
        self._model = tk.Label(text=f"{anc}", font=("Arial", 22))
        exec(f'self._model{anc} = self._model')
        self._model.pack()



TK()