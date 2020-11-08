# SUBMODULE FOR DISTANCE RELATED FUNCTIONS

# TO USE THE FUNCTIONS IN THIS SUBMODULE:
# >>> pyvect.dist

# IMPORTING REQUIRED MODULES
import numpy as np

# FUNCTIONS

# pl_line() - Returns the distance between two parallel lines.
# Syntax: vectoralg.dist.pl_line(a1_vector,a2_vector,u_vector)
# a1_vector, a2_vector - position vectors , u_vector - vector part of arbitrary constants s, t
# Return type: float
def pl_line(a1,a2,u):
    d = list(np.array(a2)-np.array(a1))
    x = np.linalg.norm(np.cross(u,d))
    return x/np.linalg.norm(u)
