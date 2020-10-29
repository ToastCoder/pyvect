# SUBMODULE FOR CENTROID RELATED FUNCTIONS

# TO USE THE FUNCTIONS IN THIS SUBMODULES:
# >>> vectoralg.cent

# IMPORTING REQUIRED MODULES
import numpy as np

# FUNCTIONS

# triangle() - Returns the centroid vector in the triangle based on the the three given positional vectors.
# Syntax: vectoralg.cent.triangle(p1,p2,p3)
# p1,p2,p3 - positional vectors of the triangle.
# Return type: float
def triangle(a,b,c):
    return 0.33*(np.array([a])+np.array([b])+np.array([c]))