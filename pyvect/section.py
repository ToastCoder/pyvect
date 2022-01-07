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
    temp1 = [i*m for i in a]
    temp2 = [i*n for i in b]
    val = m - n
    res = [(temp1[i] - temp2[i]) / val for i in range(3)]
    return res

# external() - Returns a vector using section formula using external method
# Syntax: pyvect.section.external(p1,p2,m,n)
# p1,p2 - Positional vectors
# m,n - Paramters of the ratio (m:n)
# Return type: array
def external(a,b,m,n):
    temp1 = [i*m for i in a]
    temp2 = [i*n for i in b]
    val = m + n
    res = [(temp1[i] + temp2[i]) / val for i in range(3)]
    return res
