import tkinter as tk
from tkinter import ttk
from params import CONFIG

class CFDView(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        
        # Navigation
        nav_frame = ttk.Frame(self)
        nav_frame.pack(side="top", fill="x", padx=10, pady=5)
        ttk.Button(nav_frame, text="← Home", command=lambda: self.controller.show_view("HomeView")).pack(side="left")
        ttk.Label(nav_frame, text="CFD MODULE", font=("Helvetica", 14, "bold")).pack(side="left", padx=20)

        # Notebook for CFD Modules
        self.notebook = ttk.Notebook(self)
        self.notebook.pack(expand=True, fill="both", padx=10, pady=10)

        # Fluid Properties Tab (Logic from simGUI.py)
        self.fluid_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.fluid_tab, text="Fluid Properties")
        self._setup_fluid_tab()

#-------------FLUID TAB-------------#
    def _setup_fluid_tab(self):
        # 1. Selection Pane (Left)
        selection_frame = ttk.LabelFrame(self.fluid_tab, text="Phase Selection", padding=10)
        selection_frame.pack(side="left", fill="y", padx=10, pady=10)

        self.phase_listbox = tk.Listbox(selection_frame, exportselection=False, width=12, font=("Helvetica", 10))
        self.phase_listbox.pack(expand=True, fill="both")
        
        self.phases = [k for k in CONFIG["fluid"].keys()]
        for phase in self.phases:
            self.phase_listbox.insert(tk.END, phase)
        
        # 2. Properties Container (Right)
        self.properties_container = ttk.Frame(self.fluid_tab, padding=20)
        self.properties_container.pack(side="right", expand=True, fill="both")

        # Layout Panes with extra spacing
        self.flow_pane = ttk.LabelFrame(self.properties_container, text="Flow Characteristics", padding=15)
        self.flow_pane.pack(side="top", fill="x", pady=10)

        self.mech_pane = ttk.LabelFrame(self.properties_container, text="Mechanical Properties", padding=15)
        self.mech_pane.pack(side="top", fill="x", pady=10)

        self.thermo_pane = ttk.LabelFrame(self.properties_container, text="Thermodynamic Properties", padding=15)
        self.thermo_pane.pack(side="top", fill="x", pady=10)

        self.vars = {}
        self.phase_listbox.bind("<<ListboxSelect>>", self._on_phase_change)
        self.phase_listbox.selection_set(0)
        self._on_phase_change()

    def _on_phase_change(self, event=None):
        selection = self.phase_listbox.curselection()
        if not selection: return
        phase_name = self.phase_listbox.get(selection[0])
        phase_data = CONFIG["fluid"][phase_name]

        for pane in [self.flow_pane, self.mech_pane, self.thermo_pane]:
            for child in pane.winfo_children(): child.destroy()

        self._setup_flow_pane()
        self._build_pane(self.mech_pane, phase_data["mechanical_params"])
        self._build_pane(self.thermo_pane, phase_data["thermodynamic_params"])
        
    def _setup_flow_pane(self):
        ttk.Label(self.flow_pane, text="Flow Type:", font=("Helvetica", 10, "bold")).grid(row=0, column=0, sticky="w", padx=5, pady=5)

        flow_types = list(CONFIG["Flow"].keys())
        self.flow_type_var = tk.StringVar(value=flow_types[0])
        self.vars["--flow_type"] = self.flow_type_var

        flow_cb = ttk.Combobox(self.flow_pane, textvariable=self.flow_type_var, values=flow_types, state="readonly", width=15)
        flow_cb.grid(row=0, column=1, sticky="w", padx=10, pady=5)
        flow_cb.bind("<<ComboboxSelected>>", self._on_flow_type_change)

        # Container for dynamic flow parameters (--L)
        self.flow_params_frame = ttk.Frame(self.flow_pane)
        self.flow_params_frame.grid(row=1, column=0, columnspan=3, sticky="ew", pady=5)

        # Message label for Re limits
        self.re_limit_label = ttk.Label(self.flow_pane, text="", font=("Helvetica", 9, "italic"), foreground="gray")
        self.re_limit_label.grid(row=2, column=0, columnspan=3, sticky="w", padx=5, pady=5)

        self._on_flow_type_change()

    def _on_flow_type_change(self, event=None):
        for child in self.flow_params_frame.winfo_children(): child.destroy()

        flow_type = self.flow_type_var.get()
        info = CONFIG["Flow"][flow_type]
        self.re_limit_label.config(text=info["message"])

        flag = "--L"
        l_config = info[flag]
        
        # Render Symbol and Italicized Description
        label_frame = ttk.Frame(self.flow_params_frame)
        label_frame.grid(row=0, column=0, sticky="w", padx=5, pady=5)
        
        ttk.Label(label_frame, text=l_config["symbol"], font=("Helvetica", 11, "bold")).pack(side="left")
        ttk.Label(label_frame, text=f" ({l_config['description']})", font=("Helvetica", 9, "italic")).pack(side="left")

        var = tk.StringVar(value=l_config["default"])
        self.vars[flag] = var
        ttk.Entry(self.flow_params_frame, textvariable=var, width=15).grid(row=0, column=1, padx=10, pady=5)
        ttk.Label(self.flow_params_frame, text=l_config["unit"]).grid(row=0, column=2, sticky="w", padx=5, pady=5)

    def _build_pane(self, parent, params_dict):
        for i, (flag, info) in enumerate(params_dict.items()):
            # Symbol + Description Frame
            label_frame = ttk.Frame(parent)
            label_frame.grid(row=i, column=0, sticky="w", padx=5, pady=8)
            
            ttk.Label(label_frame, text=info["symbol"], font=("Helvetica", 11, "bold"), width=4).pack(side="left")
            ttk.Label(label_frame, text=f" ({info['description']})", font=("Helvetica", 9, "italic")).pack(side="left")
            
            default_val = info["default"]
            if default_val in ["True", "False"]:
                # Handle Boolean flags as Checkbuttons
                var = tk.BooleanVar(value=(default_val == "True"))
                self.vars[flag] = var
                ttk.Checkbutton(parent, variable=var).grid(row=i, column=1, sticky="w", padx=10, pady=8)
            else:
                # Handle Numeric/Text flags as Entries
                var = tk.StringVar(value=default_val)
                self.vars[flag] = var
                ttk.Entry(parent, textvariable=var, width=15).grid(row=i, column=1, padx=10, pady=8)
            
            ttk.Label(parent, text=info["unit"]).grid(row=i, column=2, sticky="w", padx=5, pady=8)

#-------------MESH TAB-------------#
#-------------BOUNDARY TAB-------------#
