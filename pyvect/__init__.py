# Module name: Pyvect
# Short description: Pyvect is a open source python module created for the purpose of simplifying the vector calculations such as finding the angle between vectors, projection of one vector over the other and much more...!
# Developers: Vigneshwar Ravichandar(@ToastCoder), Moulishankar M R (@Moulishankar10), Vishal Balaji Sivaraman (@The-SocialLion) 
# Contact email address: vicky.pcbasic@gmail.com, moulishankarmr@gmail.com, vishalsivaraman5@gmail.com
# Modules required: numpy

# Command to install pyvect:
# >>> pip install pyvect

# Essential modules
import numpy as np

# Importing Submodules
from . import area
from .area import *

from . import cent
from .cent import *

from . import dist
from .dist import *

from . import prod
from .prod import *


# dot() - Returns the dot product of the two given vectors.
# Syntax: pyvect.dot(vector_1,vector_2)
# vector_1 - First vector , vector_2 - Second vector
# Return type: int
def dot(x,y):
    return np.dot(x,y)

# cross() - Returns the cross product (or) vector of the two given vectors.
# Syntax: pyvect.cross(vector_1,vector_2)
# vector_1 - First vector , vector_2 - Second vector
# Return type: array
def cross(x,y):
    return np.cross(x,y)

# angle() - Returns the angle formed by the two vectors in degrees.
# Syntax: pyvect.angle(vector_1,vector_2)
# vector_1 - First vector , vector_2 - Second vector
# Return type: float
def angle(x,y):
    return np.arccos(np.dot(x,y)/(np.linalg.norm(x)*np.linalg.norm(y)))

# projection() - Returns the projection formed by first vector to the second vector.
# Syntax: pyvect.projection(vector_1,vector_2)
# vector_1 - First vector , vector_2 - Second vector
# Return type: float
def projection(x,y):
    return np.dot(x,y)/np.linalg.norm(y)

# isperpendicular() - Returns True if two vectors are perpendicular to each other. (i.e) Dot product of the two vectors is zero.
# Syntax: pyvect.isperpendicular(vector_1,vector_2)
# vector_1 - First vector , vector_2 - Second vector
# Return type: bool
def isperpendicular(x,y):
    return np.dot(x,y) == 0

# iscollinear() - Returns True if two vectors are collinear. (i.e) Cross product of the two vectors is zero.
# Syntax: pyvect.iscollinear(vector_1,vector_2)
# vector_1 - First vector , vector_2 - Second vector
# Return type: bool
def iscollinear (x,y):
    return any(np.cross(x,y)) == 0

# unit_vector() - Returns the unit vector of the given vector.
# Syntax: pyvect.unit_vector(vector_1)
# vector_1 - Vector provided to the function
# Return type: array
def unit_vector(x):
    return x/np.linalg.norm(x)

# unit_normal() - Returns the unit normal vector of given two vectors.
# Syntax: pyvect.unit_normal(vector1,vector2)
# vector_1 - First vector , vector_2 - Second vector
# Return type: array
# Note: First value of the returned list - Postive value of the unit normal
#      Second value of the returned list - Negative value of the unit normal
#      since the sign of unit normal is plus or minus.
def unit_normal(x,y):
    return [np.cross(x,y)/np.linalg.norm(np.cross(x,y)),np.cross(x,y)/np.linalg.norm(np.cross(x,y))*-1]

# bisector() - Returns a vector in the direction of the bisector of the angle between two vectors.
# Syntax: pyvect.bisector(vector_1,vector_2)
# vector_1 - First vector , vector_2 - Second vector
# Return type: array
def bisector(a,b):
    return unit_vector(a)+unit_vector(b)

# pos_vector() - Returns a position vector between any two given vectors.
# Syntax: pyvect.pos_vector(vector_1,vector_2)
# vector_1 - First vector , vector_2 - Second vector.
# Return type: array
def pos_vector(a,b):
    return 0.5*(np.array([a])+np.array([b]))

# iscoplanar() - Returns the boolean value (True) if the given three vectors satisfy the condition.
# Syntax: pyvect.iscoplanar(vector_1,vector_2,vector_3)
# vector_1 - First vector , vector_2 - Second vector , vector_3 - Third vector.
# Return type: bool
def iscoplanar(a,b,c):
    return np.dot(np.cross(a,b),c)==0

# reciprocal() - Returns three reciprocal vector for the given three vectors.
# Syntax: pyvect.reciprocal(vector_1,vector_2,vector_3)
# vector_1 - First vector , vector_2 - Second vector , vector_3 - Third vector.
# Return type: array
def reciprocal(a,b,c):
    l=[]
    l.append((np.cross(b,c)/np.dot([np.cross(a,b)],c)))
    l.append((np.cross(c,a)/np.dot([np.cross(a,b)],c)))
    l.append((np.cross(a,b)/np.dot([np.cross(a,b)],c)))
    return np.array([l])

# max_value() - Returns the maximum value between any two given vectors.
# Syntax: pyvect.max_value(vector_1,vector_2)
# vector_1 - First vector , vector_2 - Second vector.
# Return type: int
def max_value(a,b):
    return np.linalg.norm(a)*np.linalg.norm(b)

# min_value() - Returns the minimum value between any two given vectors.
# Syntax: pyvect.min_value(vector_1,vector_2)
# vector_1 - First vector , vector_2 - Second vector.
# Return type: int
def min_value(a,b):
    return -1*(np.linalg.norm(a)*np.linalg.norm(b))