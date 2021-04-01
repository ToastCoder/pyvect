# SUBMODULE FOR SECTION VECTOR OPERATIONS

# TO USE THE FUNCTIONS IN THIS SUBMODULE
# >>> pyvect.section

# IMPORTING REQUIRED MODULES
import numpy as np

# FUNCTIONS

# internal() - Returns a vector using section formula using internal method
# Syntax: pyvect.section.internal(p1,p2,m,n)
# p1,p2 - Positional vectors
# m,n - Paramters of the ratio (m:n)
# Return type: array
def internal(a,b,m,n):
    return ((m*np.array([a]))-(n*np.array([b]))/(m-n))

# external() - Returns a vector using section formula using external method
# Syntax: pyvect.section.external(p1,p2,m,n)
# p1,p2 - Positional vectors
# m,n - Paramters of the ratio (m:n)
# Return type: array
def external(a,b,m,n):
    return ((m*np.array([a]))+(n*np.array([b]))/(m+n))