"""Storing all the entries we desire for every module"""
CONFIG = {
    "Flow" : { # To give 
        "External": {
            "message": "Laminar Flow up to Re~50,000", 
            "--L": {"symbol": "L", "description": "Characteristic Length", "unit": "m", "default": "1"}
        },
        "Internal": {
            "message": "Laminar Flow up to Re~2,300", 
            "--L" : {"symbol": "D", "description": "Hydraulic Diameter", "unit": "m", "default": "0.2"}
        }
    },
    "fluid": {
        "Gas": { # Default values for Air at NTP
            "mechanical_params":{
                "--v": {"symbol": "U∞", "description": "Velocity", "unit": "m/s", "default": "10"},
                "--rho": {"symbol": "ρ", "description": "Density", "unit": "kg/m³", "default": "1.204"},
                "--mu": {"symbol": "μ", "description": "Dynamic Viscosity", "unit": "Pa·s", "default": "1.825e-5"},
                "--p": {"symbol": "p", "description": "Pressure", "unit": "Pa", "default": "101325"},
                "--sigma": {"symbol": "σ", "description": "Surface Tension", "unit": "N/m", "default": "0"},
                "--comp" : {"symbol": "Com.", "description": "Compressible Gas", "unit": "", "default": "False"}
            },
            "thermodynamic_params":{
                "--temp": {"symbol": "T", "description": "Temperature", "unit": "K", "default": "293.15"},
                "--mol": {"symbol": "M", "description": "Molar Mass", "unit": "g/mol", "default": "28.97"},
                "--cp": {"symbol": "Cp", "description": "Specific Heat", "unit": "J/kg·K", "default": "1007"},
                "--cv": {"symbol": "Cv", "description": "Specific Heat", "unit": "J/kg·K", "default": "718"},
                "--k": {"symbol": "k", "description": "Thermal Conductivity", "unit": "W/m·K", "default": "0.026"},
                "--perfG": {"symbol": "Perf.", "description": "Perfect Gas", "unit": "", "default": "True"}
            }
        },
        "Liquid": {# Default values of Water at 4°C
            "mechanical_params":{ 
                "--v": {"symbol": "v", "description": "Velocity", "unit": "m/s", "default": "1"},
                "--rho": {"symbol": "ρ", "description": "Density", "unit": "kg/m³", "default": "1000"},
                "--mu": {"symbol": "μ", "description": "Dynamic Viscosity", "unit": "Pa·s", "default": "1.57e-3"},
                "--p": {"symbol": "p", "description": "Pressure", "unit": "Pa", "default": "101325"},
                "--sigma": {"symbol": "σ", "description": "Surface Tension", "unit": "N/m", "default": "0.0728"}
            },
            "thermodynamic_params":{
                "--temp": {"symbol": "T", "description": "Temperature", "unit": "K", "default": "277.13"},
                "--mol": {"symbol": "M", "description": "Molar Mass", "unit": "g/mol", "default": "18.015"},
                "--cp": {"symbol": "Cp", "description": "Specific Heat", "unit": "J/kg·K", "default": "4184"},
                "--k": {"symbol": "k", "description": "Thermal Conductivity", "unit": "W/m·K", "default": "0.598"},
                "--perfL": {"symbol": "Perf.", "description": "Perfect Liquid", "unit": "", "default": "True"}
            }
        }
    }
}
