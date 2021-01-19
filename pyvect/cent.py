# SUBMODULE FOR CENTROID RELATED FUNCTIONS

# TO USE THE FUNCTIONS IN THIS SUBMODULE:
# >>> pyvect.cent

# IMPORTING REQUIRED MODULES
import numpy as np

# FUNCTIONS

# triangle() - Returns the centroid vector in the triangle based on the the three given positional vectors.
# Syntax: pyvect.cent.triangle(p1,p2,p3)
# p1,p2,p3 - positional vectors of the triangle.
# Return type: array
def triangle(a,b,c):
    return 0.33*(np.array(a)+np.array(b)+np.array(c))

# tetrahedron() - Returns the centroid vector in the tetrahedron based on the the four given positional vectors.
# Syntax: pyvect.cent.tetrahedron(p1,p2,p3,p4)
# p1,p2,p3,p4 - positional vectors of the tetrahedron.
# Return type: array
def tetrahedron(a,b,c,d):
    return 0.25*(np.array(a)+np.array(b)+np.array(c)+np.array(d))