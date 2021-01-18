# SUBMODULE FOR DISTANCE RELATED FUNCTIONS

# TO USE THE FUNCTIONS IN THIS SUBMODULE:
# >>> pyvect.dist

# IMPORTING REQUIRED MODULES
import numpy as np

# FUNCTIONS

# pl_line() - Returns the distance between two parallel lines.
# Syntax: pyvect.dist.pl_line(a1_vector,a2_vector,u_vector)
# a1_vector, a2_vector - position vectors , u_vector - vector part of arbitrary constants s, t
# Return type: float
def pl_line(a1,a2,u):
    d = list(np.array(a2)-np.array(a1))
    x = np.linalg.norm(np.cross(u,d))
    return x/np.linalg.norm(u)

# sk_line() - Returns the distance between two skew lines.
# Syntax: pyvect.dist.sk_line(a1_vector,a2_vector,u_vector,v_vector)
# a1_vector, a2_vector - position vectors , u_vector - vector part of arbitrary constant t , v_vector - vector part of arbitrary constant s
# Return type: float
def sk_line(a1,a2,u,v):
    x = np.array([list(np.array(a2)-np.array(a1)),u,v])
    return abs(np.linalg.det(x))/np.linalg.norm(np.cross(u,v))

# pt_plane() - Returns the distance between a point and a plane.
# Syntax: pyvect.dist.pt_plane(x_co_ordinate,y_co_ordinate,z_co_ordinate,x_coeff,y_coeff,z_coeff,constant)
# x_co_ordinate - x co-ordinate value of the point, y_co_ordinate - y co-ordinate value of the point, z_co_ordinate - z co-ordinate value of the point 
# x_coeff - coefficient of x in the plane equation, y_coeff - coefficient of y in the plane equation, z_coeff - coefficient of z in the plane equation,
# constant - constant value of plane equation.
# Return type: float
def pt_plane(x,y,z,a,b,c,d):
    return abs(((a*x)+(b*y)+(c*z)+d)/(((a**2)+(b**2)+(c**2))**0.5))

# or_plane() - Returns the distance between origin and a plane.
# Syntax: pyvect.dist.or_plane(x_coeff,y_coeff,z_coeff,constant)
# x_coeff - coefficient of x in the plane equation, y_coeff - coefficient of y in the plane equation, z_coeff - coefficient of z in the plane equation,
# constant - constant value of plane equation.
# Return type: array
def or_plane(a,b,c,d):
    return abs(np.array([d])/(((a**2)+(b**2)+(c**2))**0.5))

# pl_planes() - Returns the distance between two parallel planes.
# Syntax: pyvect.dist.pl_planes(x_coeff,y_coeff,z_coeff,constant1,constant2)
# x_coeff - coefficient of x in the plane equation, y_coeff - coefficient of y in the plane equation, z_coeff - coefficient of z in the plane equation,
# constant1 - constant value of first plane.
# constant2 - constant value of second plane.
# Return type: float
def pl_planes(a,b,c,d1,d2):
     return abs((np.array([d1])-np.array([d2]))[0]/(((a**2)+(b**2)+(c**2))**0.5))

# distance() - Returns the magnitude of vector.
# Syntax: pyvect.dist.distance(x1,x2,y1,y2,z1,z2)
# x1 - x_co_ordinate of first vector, y1 - y_co_ordinate of first vector, z1 - z_co_ordinate of first vector
# x2 - x_co_ordinate of second vector, y2 - x_co_ordinate of second vector, z2 - z_co_ordinate of second vector
# Return type: float
def distance(x1,x2,y1,y2,z1,z2):
    return abs((abs(x2-x1)**2)+(abs(y2-y1)**2)+(abs(z2-z1)**2))**0.5