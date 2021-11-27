# SUBMODULE FOR AREA FUNCTIONS

# TO USE THE FUNCTIONS IN THIS SUBMODULE:
# >>> pyvect.area

# IMPORTING REQUIRED MODULES
from . import __init__
from .__init__ import *

# FUNCTIONS

# triangle_adj() - Returns the area of a triangle where the two adjacent sides of the triangle are given.
# Syntax: pyvect.area.triangle_adj(vector_1,vector_2)
# vector_1 - First adjacent side , vector_2 - Second adjacent side
# Return type: float
def triangle_adj(a,b):
    return modVector(cross(a,b)) * 0.5

# triangle_pos() - Returns the area of the triangle based on the given three positional vectors.
# Syntax: pyvect.area.triangle_pos(p1,p2,p3)
# p1,p2,p3 - positional vectors of the triangle.
# Return type: float
def triangle_pos(a,b,c):
    res = []
    for i in range(3):
        res.append(cross(a, b)[i] + cross(b, c)[i] + cross(c, a)[i])
    return 0.5 * modVector(res)

# quad() - Returns the area of a quadrilateral based on the diagonal vectors.
# Syntax: pyvect.area.quad(diagonal_1,diagonal_2)
# diagonal_1 - Primary diagonal of the quadrilateral, diagonal_2 - Secondary diagonal of the quadrilateral.
# Return type: float
def quad(a,b):
    return 0.5 * modVector(cross(a,b))

# parallelogram() - Returns the area of parallelogram based on the two adjacent vectors.
# Syntax: pyvect.area.parallelogram(vector_1,vector_2)
# vector_1 - First vector , vector_2 - Second vector.
# Return type: float
def parallelogram(a,b):
    return modVector(cross(a,b))

# tetrahedron() - Returns the area of tetrahedron based on the three position vectors.
# Syntax: pyvect.area.tetrahedron(p1,p2,p3)
# p1,p2,p3 - positional vectors of the tetrahedron.
# Return type: float
def tetrahedron(a,b,c):
    res = 0.1666 * dot(cross(a,b),c)
    return res if res > 0 else res
