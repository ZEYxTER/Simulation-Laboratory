# General Imports
import tkinter as tk
from tkinter import ttk, Menu

# View Imports
from views import HomeView, CFDView, FEMView, ControlView

class simLabGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        
        # --------- Window Geometry --------- #
        self.title("Simulator Lab")
        self.geometry("1100x1200")
        
        # --------- Main Container --------- #
        # This container will hold all our views stacked on top of each other
        self.container = tk.Frame(self)
        self.container.pack(side="top", fill="both", expand=True)
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)

        # --------- Menu Bar --------- #
        self._setup_menu()

        # --------- Initialize Views --------- #
        self.views = {}
        for ViewClass in (HomeView, CFDView, FEMView, ControlView):
            view_name = ViewClass.__name__
            frame = ViewClass(parent=self.container, controller=self)
            self.views[view_name] = frame
            # Grid them all in the same location (stacking)
            frame.grid(row=0, column=0, sticky="nsew")

        # Start at the Home View
        self.show_view("HomeView")

    def _setup_menu(self):
        """Standard attached menu bar (no Toplevel junk)"""
        self.option_add('*tearOff', False)
        self.menubar = Menu(self)
        self.config(menu=self.menubar)
        
        # File Menu
        file_menu = Menu(self.menubar)
        self.menubar.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="Home", command=lambda: self.show_view("HomeView"))
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.quit)

    def show_view(self, name):
        """Show a frame for the given view name by raising it to the top"""
        frame = self.views[name]
        frame.tkraise()

if __name__ == "__main__":
    app = simLabGUI()
    app.mainloop()
