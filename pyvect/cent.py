# SUBMODULE FOR CENTROID RELATED FUNCTIONS

# TO USE THE FUNCTIONS IN THIS SUBMODULE:
# >>> pyvect.cent

# FUNCTIONS

# triangle() - Returns the centroid vector in the triangle based on the the three given positional vectors.
# Syntax: pyvect.cent.triangle(p1,p2,p3)
# p1,p2,p3 - positional vectors of the triangle.
# Return type: array
def triangle(a,b,c):
    res = []
    for i in range(3):
        res.append((a[i] + b[i] + c[i]) * 0.33)
    return res


# tetrahedron() - Returns the centroid vector in the tetrahedron based on the the four given positional vectors.
# Syntax: pyvect.cent.tetrahedron(p1,p2,p3,p4)
# p1,p2,p3,p4 - positional vectors of the tetrahedron.
# Return type: array
def tetrahedron(a,b,c,d):
    res = []
    for i in range(3):
        res.append((a[i] + b[i] + c[i] + d[i]) * 0.25)
    return res
