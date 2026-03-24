from tkinter import *
from tkinter import ttk
from params import CONFIG

class miAmor():
    def __init__(self):
        self.wakanda = "hello"

if __name__ == "__main__":
    modules = [
            ("CFD", "CFDView", "CFD.jpg"),
            ("FEM", "FEMView", "FEM.jpeg"),
            ("CONTROL", "ControlView", "CONTROL.png")
    ]

    for (label, view, pic) in modules:
        print(label)