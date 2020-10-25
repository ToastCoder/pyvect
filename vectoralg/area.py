# SUBMODULE FOR AREA FUNCTIONS

# TO USE THE FUNCTIONS IN THIS SUBMODULES:
# >>> vectoralg.area

# IMPORTING REQUIRED MODULES
import numpy as np

# FUNCTIONS

# triangle_adj() - Returns the area of a triangle where the two adjacent sides of the triangle are given.
# Syntax: vectoralg.area.triangle_adj(vector_1,vector_2)
# vector_1 - First adjacent side , vector_2 - Second adjacent side
# Return type: float
def triangle_adj(x,y):
    return abs(0.5*np.linalg.norm(np.cross(x,y)))

def triangle_pos(a,b,c):
    return abs(0.5*np.linalg.norm(np.cross(a,b)+np.cross(b,c)+np.cross(c,a)))