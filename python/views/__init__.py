# This file marks the 'views' directory as a Python Package.
# It acts as a "Receptionist" (Facade Pattern) for the directory.

# --- EXPOSURE DECLARATIONS ---
# By importing these classes here, we "expose" them to the package level.
from .home_view import HomeView
from .cfd_view import CFDView
from .fem_view import FEMView
from .ctrl_view import ControlView

# --- INTENTION ---
# 1. Clean Imports: Allows other files to use 'from views import HomeView' 
#    instead of reaching deep into 'from views.home_view import HomeView'.
# 2. Encapsulation: If we rename a file (e.g., 'home_view.py' -> 'main_menu.py'), 
#    we only update it here. The rest of the app doesn't need to change.
# 3. Organization: Keeps the 'simLabGUI.py' (Main Controller) clean of 
#    repetitive import logic.
