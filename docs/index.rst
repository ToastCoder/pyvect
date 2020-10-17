Introduction
====================================

Vectoralg (or) Vector Algebra functions is a open source python module created for the purpose of simplifying the vector calculations such as finding the angle between vectors, projection of one vector over the other and much more...!

vectoralg.dot()
====================================

About
------------------------------------

Returns the dot product of the two given vectors.

Syntax 
------------------------------------

>>> dot(vector_1,vector_2)

vector_1 -First vector

vector_2 - Second vector

Return type
-------------------------------------

int

Example
-------------------------------------

>>> vectoralg.dot([2,3,4],[1,5,3])


Output
-------------------------------------
+-----------------------------------+
| 29                                |
+-----------------------------------+

vectoralg.cross()
=====================================

About
-------------------------------------

Returns the cross product (or) vector of the two given vectors.

Syntax
-------------------------------------

>>> cross(vector_1,vector_2)

vector_1 - First vector

vector_2 - Second vector

Return type
--------------------------------------

array


Example
--------------------------------------

>>> vectoralg.cross([2,3,4],[1,5,3])

Output
--------------------------------------

+------------------------------------+
| array([-11,-2,7])                  |
+------------------------------------+

vectoralg.angle()
======================================

About
--------------------------------------

Returns the angle formed by the two vectors in degrees.

Syntax
--------------------------------------

>>> angle(vector_1,vector_2)

vector_1 - First vector

vector_2 - Second vector

Return type
--------------------------------------

float


Example
---------------------------------------

>>> vectoralg.angle([1,-1,0],[0,1,-1])