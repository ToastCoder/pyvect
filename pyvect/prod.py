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

# s4() - Returns the scalar product of the given four vectors.
# Syntax: pyvect.prod.s4(vector_1,vector_2,vector_3,vector_4)
# vector_1 - First vector , vector_2 - Second vector , vector_3 - Third vector , vector_4 - Fourth vector
# Return type: int
def s4(w,x,y,z):
    return np.dot(np.cross(w,x),np.cross(y,z))

# v3() - Returns the vector triple product of the given three vectors.
# Syntax: pyvect.prod.v3(vector_1,vector_2,vector_3)
# vector_1 - First vector , vector_2 - Second vector , vector_3 - Third vector
# Return type: array
def v3(x,y,z):
    return np.cross(np.cross(x,y),z)

# v4() - Returns the vector product of the given four vectors.
# Syntax: pyvect.prod.v4(vector_1,vector_2,vector_3,vector_4)
# vector_1 - First vector , vector_2 - Second vector , vector_3 - Third vector , vector_4 - Fourth vector
# Return type: array
def v4(w,x,y,z):
    return np.cross(np.cross(np.array(w),np.array(x)),np.cross(np.array(y),np.array(z)))