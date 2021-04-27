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
# Syntax: pyvect.dist.pt_plane(point,plane)
# point - any point containing x,y and z co-ordinates
# plane - a plane equation containing x,y,z co-efficients and a constant value refers the distance from origin
# Return type: float
def pt_plane(point,plane):
    return abs(((plane[0]*point[0])+(plane[1]*point[1])+(plane[2]*point[2])+plane[3])/(((plane[0]**2)+(plane[1]**2)+(plane[2]**2))**0.5))

# or_plane() - Returns the distance between origin and a plane.
# Syntax: pyvect.dist.or_plane(x_coeff,y_coeff,z_coeff,constant)
# x_coeff - coefficient of x in the plane equation, y_coeff - coefficient of y in the plane equation, z_coeff - coefficient of z in the plane equation,
# constant - constant value of plane equation.
# Return type: float
def or_plane(a,b,c,d):
    return abs(d/(((a**2)+(b**2)+(c**2))**0.5))

# pl_planes() - Returns the distance between two parallel planes.
# Syntax: pyvect.dist.pl_planes(x_coeff,y_coeff,z_coeff,constant1,constant2)
# x_coeff - coefficient of x in the plane equation, y_coeff - coefficient of y in the plane equation, z_coeff - coefficient of z in the plane equation,
# constant1 - constant value of first plane.
# constant2 - constant value of second plane.
# Return type: float
def pl_planes(a,b,c,d1,d2):
     return abs((d1-d2)/(((a**2)+(b**2)+(c**2))**0.5))

# distance() - Returns the distance between two vectors.
# Syntax: pyvect.dist.distance(x1,x2,y1,y2,z1,z2)
# x1 - x_co_ordinate of first vector, y1 - y_co_ordinate of first vector, z1 - z_co_ordinate of first vector
# x2 - x_co_ordinate of second vector, y2 - x_co_ordinate of second vector, z2 - z_co_ordinate of second vector
# Return type: float
def distance(x1,y1,z1,x2,y2,z2):
    return abs((x2-x1)**2+((y2-y1)**2)+((z2-z1)**2))**0.5