# SUBMODULE FOR SECTION VECTOR OPERATIONS

# TO USE THE FUNCTIONS IN THIS SUBMODULE
# >>> vectoralg.section

# IMPORTING REQUIRED MODULES
import numpy as np

# FUNCTIONS

# internal() - Returns a vector using section formula using internal method
# Syntax: vectoralg.section.internal(p1,p2,m,n)
# p1,p2 - Positional vectors
# m,n - Paramters of the ratio (m:n)
# Return type: array
def internal(a,b,m,n):
    return ((m*np.array([a]))-(n*np.array([b]))/(m-n))

# internal() - Returns a vector using section formula using external method
# Syntax: vectoralg.section.external(p1,p2,m,n)
# p1,p2 - Positional vectors
# m,n - Paramters of the ratio (m:n)
# Return type: array
def external(a,b,m,n):
    return ((m*np.array([a]))+(n*np.array([b]))/(m+n))
  


