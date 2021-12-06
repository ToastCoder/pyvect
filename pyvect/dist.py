# SUBMODULE FOR DISTANCE RELATED FUNCTIONS

# TO USE THE FUNCTIONS IN THIS SUBMODULE:
# >>> pyvect.dist

# IMPORTING REQUIRED MODULES
from . import __init__
from .__init__ import *

# FUNCTIONS

# pl_line() - Returns the distance between two parallel lines.
# Syntax: pyvect.dist.pl_line(a1_vector,a2_vector,u_vector)
# a1_vector, a2_vector - position vectors , u_vector - vector part of arbitrary constants s, t
# Return type: float
def pl_line(a1,a2,u):
    diff = [a2[i] - a1[i] for i in range(3)]
    val = modVector(cross(u, diff))
    return val / modVector(u)

# sk_line() - Returns the distance between two skew lines.
# Syntax: pyvect.dist.sk_line(a1_vector,a2_vector,u_vector,v_vector)
# a1_vector, a2_vector - position vectors , u_vector - vector part of arbitrary constant t , v_vector - vector part of arbitrary constant s
# Return type: float
def sk_line(a1,a2,u,v):
    temp = [a2[i] - a1[i] for i in range(3)]
    temp += u + v
    det_val = (temp[0] * (u[1]*v[2] - (u[2]*v[1]))) - (temp[1] * (u[0]*v[2] - (u[2]*v[0]))) + (temp[2] * (u[0]*v[1] - (u[1]*v[0])))
    return abs(det_val / modVector(cross(u, v)))

# pt_plane() - Returns the distance between a point and a plane.
# Syntax: pyvect.dist.pt_plane(point,plane)
# point - any point containing x,y and z co-ordinates
# plane - a plane equation containing x,y,z co-efficients and a constant value refers the distance from origin
# Return type: float
def pt_plane(point,plane):
    return abs(((plane[0]*point[0]) + (plane[1]*point[1]) + (plane[2]*point[2]) + plane[3]) / (((plane[0]**2) + (plane[1]**2) + (plane[2]**2)) ** 0.5))

# or_plane() - Returns the distance between origin and a plane.
# Syntax: pyvect.dist.or_plane(plane)
# plane - a plane equation containing x,y,z co-efficients and a constant value refers the distance from origin
# Return type: float
def or_plane(plane):
    return abs(plane[3] / (((plane[0]**2) + (plane[1]**2) + (plane[2]**2)) ** 0.5))

# pl_planes() - Returns the distance between two parallel planes.
# Syntax: pyvect.dist.pl_planes(plane1,plane2)
# plane - first plane equation containing x,y,z co-efficients and a constant value refers the distance from origin
# plane - second plane equation containing x,y,z co-efficients and a constant value refers the distance from origin
# Return type: float
def pl_planes(plane1,plane2):
    if plane1[0]%plane2[0] == 0:
        x = plane1[0] / plane2[0]
        for i in range(len(plane2)):
            plane2[i] *= x
    elif plane2[0]%plane1[0] == 0:
        x = plane2[0] / plane1[0]
        for i in range(len(plane1)):
            plane1[i] *= x
    return abs((plane2[3]-plane1[3]) / (((plane1[0]*plane2[0]) + (plane1[1]*plane2[1]) + (plane1[2]*plane2[2])) ** 0.5))

# distance() - Returns the distance between two vectors.
# Syntax: pyvect.dist.distance(vector_1,vector_2)
# vector_1 - First Vector, vector_2 - Second Vector
# Return type: float
def distance(vector_1,vector_2):
    return (((vector_2[0]-vector_1[0]) ** 2) + ((vector_2[1]-vector_1[1]) ** 2) + ((vector_1[2]-vector_2[2]) ** 2)) ** 0.5