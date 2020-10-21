# SUBMODULE FOR AREA FUNCTIONS

# TO USE THE FUNCTIONS IN THIS SUBMODULES:
# >>> vectoralg.area

# IMPORTING REQUIRED MODULES
import numpy as np

def triangle_adj(x,y):
    return abs(0.5*np.linalg.norm(np.cross(x,y)))
