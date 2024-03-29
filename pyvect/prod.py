# SUBMODULE FOR VECTOR PRODUCT AND SCALAR PRODUCT RELATED FUNCTIONS

# TO USE THE FUNCTIONS IN THIS SUBMODULES:
# >>> pyvect.prod

# IMPORTING REQUIRED MODULES
from . import __init__
from .__init__ import *

# FUNCTIONS

# s3() - Returns the scalar triple product of the given three vectors.
# Syntax: pyvect.prod.s3(vector_1,vector_2,vector_3)
# vector_1 - First vector , vector_2 - Second vector , vector_3 - Third vector
# Return type: int
def s3(x,y,z):
    return (dot(cross(x,y),z))

# s4() - Returns the scalar product of the given four vectors.
# Syntax: pyvect.prod.s4(vector_1,vector_2,vector_3,vector_4)
# vector_1 - First vector , vector_2 - Second vector , vector_3 - Third vector , vector_4 - Fourth vector
# Return type: int
def s4(w,x,y,z):
    return dot(cross(w,x),cross(y,z))

# v3() - Returns the vector triple product of the given three vectors.
# Syntax: pyvect.prod.v3(vector_1,vector_2,vector_3)
# vector_1 - First vector , vector_2 - Second vector , vector_3 - Third vector
# Return type: array
def v3(x,y,z):
    return cross(cross(x,y),z)

# v4() - Returns the vector product of the given four vectors.
# Syntax: pyvect.prod.v4(vector_1,vector_2,vector_3,vector_4)
# vector_1 - First vector , vector_2 - Second vector , vector_3 - Third vector , vector_4 - Fourth vector
# Return type: array
def v4(w,x,y,z):
    return cross(cross(w,x),cross(y,z))