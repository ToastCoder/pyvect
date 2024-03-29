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

from . import volume
from .volume import *

from . import section
from .section import *

# HELPER FUNCTION
# modVector() - Returns the modulus of a vector
# Return type: float
def modVector(x):
    return ((x[0]*x[0])+(x[1]*x[1])+(x[2]*x[2])) ** 0.5

# dot() - Returns the dot product of the two given vectors.
# Syntax: pyvect.dot(vector_1,vector_2)
# vector_1 - First vector , vector_2 - Second vector
# Return type: int
def dot(x,y):
    dot_product = 0
    for i in range(3):
        dot_product += x[i] * y[i]
    return dot_product

# cross() - Returns the cross product (or) vector of the two given vectors.
# Syntax: pyvect.cross(vector_1,vector_2)
# vector_1 - First vector , vector_2 - Second vector
# Return type: array
def cross(x,y):
    cross_product = []
    cross_product.append(x[1]*y[2] - x[2]*y[1])
    cross_product.append(-(x[0]*y[2] - x[2]*y[0]))
    cross_product.append(x[0]*y[1] - x[1]*y[0])
    return cross_product

# angle() - Returns the angle formed by the two vectors in degrees.
# Syntax: pyvect.angle(vector_1,vector_2)
# vector_1 - First vector , vector_2 - Second vector
# Return type: float
def angle(x,y):
    return np.arccos(dot(x,y)/(modVector(x)*modVector(y)))

# projection() - Returns the projection formed by first vector to the second vector.
# Syntax: pyvect.projection(vector_1,vector_2)
# vector_1 - First vector , vector_2 - Second vector
# Return type: float
def projection(x,y):
    return dot(x,y)/modVector(y)

# isperpendicular() - Returns True if two vectors are perpendicular to each other. (i.e) Dot product of the two vectors is zero.
# Syntax: pyvect.isperpendicular(vector_1,vector_2)
# vector_1 - First vector , vector_2 - Second vector
# Return type: bool
def isperpendicular(x,y):
    return dot(x,y) == 0

# iscollinear() - Returns True if two vectors are collinear. (i.e) Cross product of the two vectors is zero.
# Syntax: pyvect.iscollinear(vector_1,vector_2)
# vector_1 - First vector , vector_2 - Second vector
# Return type: bool
def iscollinear (x,y):
    return any(cross(x,y)) == 0

# unit_vector() - Returns the unit vector of the given vector.
# Syntax: pyvect.unit_vector(vector_1)
# vector_1 - Vector provided to the function
# Return type: array
def unit_vector(x):
    mod = modVector(x)
    x = [i/mod for i in x]
    return x


# unit_normal() - Returns the unit normal vector of given two vectors.
# Syntax: pyvect.unit_normal(vector1,vector2)
# vector_1 - First vector , vector_2 - Second vector
# Return type: array
# Note: First value of the returned list - Postive value of the unit normal
#      Second value of the returned list - Negative value of the unit normal
#      since the sign of unit normal is plus or minus.
def unit_normal(x,y):
    res = unit_vector(cross(x, y))
    return [res, [-i for i in res]]

# bisector() - Returns a vector in the direction of the bisector of the angle between two vectors.
# Syntax: pyvect.bisector(vector_1,vector_2)
# vector_1 - First vector , vector_2 - Second vector
# Return type: array
def bisector(a,b):
    a = unit_vector(a)
    b = unit_vector(b)
    print(a)
    print(b)
    return [a[i] + b[i] for i in range(3)]

# pos_vector() - Returns a position vector between any two given vectors.
# Syntax: pyvect.pos_vector(vector_1,vector_2)
# vector_1 - First vector , vector_2 - Second vector.
# Return type: array
def pos_vector(a,b):
    res = [int(0.5 * (a[i]+b[i])) for i in range(3)]
    return res

# iscoplanar() - Returns the boolean value (True) if the given three vectors satisfy the condition.
# Syntax: pyvect.iscoplanar(vector_1,vector_2,vector_3)
# vector_1 - First vector , vector_2 - Second vector , vector_3 - Third vector.
# Return type: bool
def iscoplanar(a,b,c):
    return dot(cross(a,b),c)==0


# reciprocal() - Returns three reciprocal vector for the given three vectors.
# Syntax: pyvect.reciprocal(vector_1,vector_2,vector_3)
# vector_1 - First vector , vector_2 - Second vector , vector_3 - Third vector.
# Return type: array
def reciprocal(a,b,c):
    res = []
    temp = dot(cross(a,b), c)
    res.append([i/temp for i in cross(b, c)])
    res.append([i/temp for i in cross(c, a)])
    res.append([i/temp for i in cross(a, b)])
    return res

# max_value() - Returns the maximum value between any two given vectors.
# Syntax: pyvect.max_value(vector_1,vector_2)
# vector_1 - First vector , vector_2 - Second vector.
# Return type: int
def max_value(a,b):
    return modVector(a) * modVector(b)

# min_value() - Returns the minimum value between any two given vectors.
# Syntax: pyvect.min_value(vector_1,vector_2)
# vector_1 - First vector , vector_2 - Second vector.
# Return type: int
def min_value(a,b):
    return -(modVector(a) * modVector(b))
