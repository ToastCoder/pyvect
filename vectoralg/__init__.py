# Module name: vectoralg
# Short description: Vectoralg (or) Vector Algebra functions is a open source python module created for the purpose of simplifying the vector calculations such as finding the angle between vectors, projection of one vector over the other and much more...!
# Developers: Vigneshwar Ravichandar(@ToastCoder), Moulishankar M R (@Moulishankar10), Vishal Balaji Sivaraman (@The-SocialLion) 
# Contact email address: vicky.pcbasic@gmail.com, moulishankarmr@gmail.com, vishalsivaraman5@gmail.com
# Modules required: numpy

# Command to install vectoralg:
# >>> pip install vectoralg

# Essential modules
import numpy as np

# dot() - Returns the dot product of the two given vectors.
# Syntax: vectoralg.dot(vector_1,vector_2)
# vector_1 - First vector , vector_2 - Second vector
# Return type: int
def dot(x,y):
    return np.dot(x,y)

# cross() - Returns the cross product (or) vector of the two given vectors.
# Syntax: vectoralg.cross(vector_1,vector_2)
# vector_1 - First vector , vector_2 - Second vector
# Return type: array
def cross(x,y):
    return np.cross(x,y)

# angle() - Returns the angle formed by the two vectors in degrees.
# Syntax: vectoralg.angle(vector_1,vector_2)
# vector_1 - First vector , vector_2 - Second vector
# Return type: float
def angle(x,y):
    return np.arccos(np.dot(x,y)/(np.linalg.norm(x)*np.linalg.norm(y)))

# projection() - Returns the projection formed by first vector to the second vector.
# Syntax: vectoralg.projection(vector_1,vector_2)
# vector_1 - First vector , vector_2 - Second vector
# Return type: float
def projection(x,y):
    return np.dot(x,y)/np.linalg.norm(y)

# isperpendicular() - Returns True if two vectors are perpendicular to each other. (i.e) Dot product of the two vectors is zero.
# Syntax: vectoralg.isperpendicular(vector_1,vector_2)
# vector_1 - First vector , vector_2 - Second vector
# Return type: bool
def isperpendicular(x,y):
    return np.dot(x,y) == 0

# iscollinear() - Returns True if two vectors are collinear. (i.e) Cross product of the two vectors is zero.
# Syntax: vectoralg.iscollinear(vector_1,vector_2)
# vector_1 - First vector , vector_2 - Second vector
# Return type: bool
def iscollinear (x,y):
    return any(np.cross(x,y)) == 0

# vector() - Returns the unit vector of the given vector.
# Syntax: vectoralg.unit_vector(vector_1)
# vector_1 - Vector provided to the function
# Return type: array
def unit_vector(x):
    return x/np.linalg.norm(x)
