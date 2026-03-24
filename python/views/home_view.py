import tkinter as tk
from tkinter import ttk
import os
from PIL import Image, ImageTk

class HomeView(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        
        # Center title
        ttk.Label(self, text="SIMULATOR LAB", font=("Helvetica", 24, "bold")).pack(pady=40)
        
        # Container for the 3 Big Buttons
        btn_container = ttk.Frame(self)
        btn_container.pack(expand=True)

        # BUTTONS Config
        # [label, view_name, image_filename]
        modules = [
            ("CFD", "CFDView", "CFD.jpg"),
            ("FEM", "FEMView", "FEM.jpeg"),
            ("CONTROL", "ControlView", "CONTROL.png")
        ]

        # Get absolute path to the root resources folder
        current_dir = os.path.dirname(os.path.abspath(__file__)) # .../python/views
        resources_dir = os.path.join(current_dir, "..", "..", "resources")

        self.images = {} # To keep references to images (prevents garbage collection)

        for (label, view_name, img_name) in modules:
            img_path = os.path.join(resources_dir, img_name)
            
            try:
                # Load and Resize image (e.g., to 300x200 or similar)
                pil_img = Image.open(img_path)
                pil_img = pil_img.resize((280, 200), Image.Resampling.LANCZOS)
                tk_img = ImageTk.PhotoImage(pil_img)
                self.images[view_name] = tk_img
                
                # Button with Image
                btn = tk.Button(btn_container, text='', image=tk_img, 
                                compound="top", # Place image on top of text
                                bg="gray", font=("Helvetica", 18, "bold"),
                                command=lambda v=view_name: self.controller.show_view(v))
                
            except Exception as e:
                # Fallback to colored button if image fails to load
                print(f"Error loading {img_name}: {e}")
                btn = tk.Button(btn_container, text=label, width=20, height=10, 
                                bg="gray", font=("Helvetica", 12, "bold"),
                                command=lambda v=view_name: self.controller.show_view(v))

            btn.pack(side="right", padx=20)
        ttk.Label(self, text="Choose a module to begin calculations", font=("Helvetica", 10, "italic")).pack(pady=20)
