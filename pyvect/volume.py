# SUBMODULE FOR VOLUME VECTOR OPERATIONS

# TO USE THE FUNCTIONS IN THIS SUBMODULE
# >>> pyvect.volume

# IMPORTING REQUIRED SUB-MODULES
from . import prod
from .prod import *

# FUNCTIONS

# parallelopiped() - Returns the volume of the parallelopiped formed by three vectors.
# Syntax: pyvect.volume.parallelopiped(vector_1,vector_2,vector_3)
# vector_1 - First vector , vector_2 - Second vector , vector_3 - Third vector
# Return type: int
def parallelopiped(x,y,z):
    return abs(s3(x,y,z))