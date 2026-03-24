import tkinter as tk
from tkinter import ttk

class FEMView(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        
        # Navigation
        nav_frame = ttk.Frame(self)
        nav_frame.pack(side="top", fill="x", padx=10, pady=5)
        ttk.Button(nav_frame, text="← Home", command=lambda: self.controller.show_view("HomeView")).pack(side="left")
        
        ttk.Label(self, text="FEM MODULE", font=("Helvetica", 18, "bold")).pack(pady=20)
        ttk.Label(self, text="Finite Element Analysis tools coming soon...", font=("Helvetica", 12, "italic")).pack(expand=True)
