# Simulator Lab
## First experience
I want it to be simple and enjoyable
First thing I want user to see is a pane with 3 options and the menu bar, the 3 options will be buttons with CFD, FEM, CONTROL and associated to pictures saved in folder '/resources'. 
When clicking a button it will go to said module with its characteristic panes and modules.
## General 
All this information calculated should be saved so that the user can open up the app in the folder of his case information and also be available to export it to an md if he wants to get the written information/calculations.
Import of stl and step files with a gui 3D visualisation.
## CFD MODULE
This app should help with calculations of nondimensional numbers, boundary condition selections, turbulence model selection, mesh requirements with hindsight of the characteristics of the flow, stagnation points... 

### FLUID TAB
- Log fluid properties 
- calculations:
    - Dimensionless numbers
    - isentropic relations 
    - stagnation points with its properties
    - compressibility analysis (GAS)
    - Pitot tube error U_{infty}

### MESH TAB
- Log biggest mesh element 1D
- calculations:
    - Hexa, tetra general surface and volume refinement (Openfoam method of cell division: V/2^n or S/2^n, being n levels of refinement)
    - Boundary Layers from:
        - Total Thickness
        - First Layer Thickness
    - Y+ Calculation
    - Y Calculation
    - U_{friction}
    - U+
    - General BL graph (x: y+ y: U+) and with given values OUR position (% of wall modelling)
    - Wall Shear Stress
    - Friction coefficient with options: 
        1. Prandtl (1927) $$\rightarrow C_f = 0.074Re_x^{-0.2}$$
        2. Granville (1977) $$\rightarrow C_f = 0.0776[log_{10}Re_x - 1.88]^{-2} + 60 Re_x^{-1}$$
        3. Schlichting $$\rightarrow C_f = [2 log_{10} Re_x - 0.65]^{-2.3}$$
        4. Kempf-Karman (1951) $$\rightarrow C_f = 0.055 Re_x^{-0.182}$$
        5. Schultz-Grunov (1940) $$\rightarrow C_f = 0.427[log_{10} Re_x - 0.407]^{-2.64}$$

### BOUNDARY TAB

### Fluid properties module

### Future fun additions
Area rule to step or stl files
Inertial calculations to geometry 
Center of gravity
 ## FEM MODULE
-- TO BE DESIGNED
 ## CONTROL SYSTEMS MODULE
-- TO BE DESIGNED

## Project Architecture
The application follows a **Model-View-Controller (MVC)** inspired architecture to ensure scalability across different engineering disciplines.

### File Structure
```text
/simulationLab
├── /cpp                 # Calculation Workhorse (High-performance logic)
│   ├── /src             
│   ├── /include         
│   └── Makefile
├── /python
│   ├── /views           # Encapsulated UI Modules (Frames)
│   │   ├── home_view.py # Entry Pane with 3-module selection
│   │   ├── cfd_view.py  # CFD specific tools & Fluid properties
│   │   └── other_views.py # FEM and Control placeholders
│   ├── simLabGUI.py     # Main Controller (App Shell & View Switcher)
│   ├── params.py        # Centralized CONFIG for data-driven UI
└── /resources           # Images and Icons
```

### Class Management
- **simLabGUI (The Shell)**: Manages the main window, global menus, and the stacking/raising of different views using `tkraise()`.
- **Views (The Modules)**: Each module (CFD, FEM, Control) is an independent `tk.Frame`. This encapsulation allows developers to work on one module without affecting the others.

## PYTHON 
General gui handling and modular view management.
## C++ 
Calculation workhorse for heavy aerodynamic and structural physics.
Need to change Makefile, it is not updated.

## GITHUB inspiration module
[Simulator Calculator](https://github.com/ZEYxTER/SimulationCalculator)