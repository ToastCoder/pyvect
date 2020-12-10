# SUBMODULE FOR VECTOR PRODUCT AND SCALAR PRODUCT RELATED FUNCTIONS

# TO USE THE FUNCTIONS IN THIS SUBMODULES:
# >>> pyvect.prod

# IMPORTING REQUIRED MODULES
import numpy as np

# FUNCTIONS

# s3() - Returns the scalar triple product of the given three vectors.
# Syntax: pyvect.prod.s3(vector_1,vector_2,vector_3)
# vector_1 - First vector , vector_2 - Second vector , vector_3 - Third vector
# Return type: int
def s3(x,y,z):
    return (np.dot(np.cross(x,y),z))