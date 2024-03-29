Introduction
====================================

Pyvect is a open source python module created for the purpose of simplifying the vector calculations such as finding the angle between vectors, projection of one vector over the other and much more...!

pyvect.dot()
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

>>> pyvect.dot([2,3,4],[1,5,3])


Output
-------------------------------------
+-----------------------------------+
| 29                                |
+-----------------------------------+

pyvect.cross()
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

>>> pyvect.cross([2,3,4],[1,5,3])

Output
--------------------------------------

+------------------------------------+
| array([-11,-2,7])                  |
+------------------------------------+

pyvect.angle()
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

>>> pyvect.angle([1,-1,0],[0,1,-1])

Output
---------------------------------------

+-------------------------------------+
| 2.0943951023931953                  |
+-------------------------------------+

pyvect.projection()
=======================================

About
---------------------------------------

Returns the projection formed by first vector to the second vector.

Syntax
---------------------------------------

>>> projection(vector_1,vector_2)

vector_1 - First vector

vector_2 - Second vector

Return type
---------------------------------------

float

Example
---------------------------------------

>>> pyvect.projection([1,2,3],[4,5,6])

Output
----------------------------------------

+--------------------------------------+
| 3.6467384467084143                   |
+--------------------------------------+

pyvect.isperpendicular()
========================================

About
-----------------------------------------

Returns True if two vectors are perpendicular to each other. (i.e) Dot product of the two vectors is zero.

Syntax
-----------------------------------------

>>> isperpendicular(vector_1,vector_2)

vector_1 - First vector

vector_2 - Second vector

Return type
------------------------------------------

bool

Example
------------------------------------------

>>> pyvect.isperpendicular([-3,4,-7],[2,-51,-30])

Output
-------------------------------------------

+-----------------------------------------+
| True                                    |
+-----------------------------------------+

pyvect.iscollinear()
============================================

About
--------------------------------------------

Returns True if two vectors are collinear. (i.e) Cross product of the two vectors is zero.

Syntax
----------------------------------------------

>>> iscollinear(vector_1,vector_2)

vector_1 - First vector

vector_2 - Second vector

Return type
------------------------------------------------
bool

Example
------------------------------------------------

>>> pyvect.iscollinear([1,2,3],[2,4,6])

Output
-------------------------------------------------

+------------------------------------------------+
| True                                           |
+------------------------------------------------+

pyvect.unit_vector()
==================================================

About
--------------------------------------------------

Returns the unit vector of the given vector.

Syntax
--------------------------------------------------

>>> unit_vector(vector_1)

vector_1 - Vector provided to the function

Return type
---------------------------------------------------

array

Example
---------------------------------------------------

>>> pyvect.unit_vector([2,3,7])

Output
---------------------------------------------------

+-------------------------------------------------+
| array([0.25400025, 0.38100038, 0.88900089])     |
+-------------------------------------------------+

pyvect.unit_normal()
==================================================

About
--------------------------------------------------

Returns the unit normal vector of given two vectors

Syntax
--------------------------------------------------

>>> unit_normal(vector1,vector2)

vector_1 - First vector 

vector_2 - Second vector

Return type
---------------------------------------------------

array

Example
---------------------------------------------------

>>> pyvect.unit_normal([2,1,1],[1,2,1])

Output
---------------------------------------------------

+--------------------------------------------------------------------------------------------------+
| [array([-0.30151134, -0.30151134,  0.90453403]), array([ 0.30151134,  0.30151134, -0.90453403])] | 
+--------------------------------------------------------------------------------------------------+

pyvect.bisector()
==================================================

About
---------------------------------------------------

Returns a vector in the direction of the bisector of the angle between two vectors.

Syntax
----------------------------------------------------

>>> bisector(vector_1,vector_2)

vector_1 - First vector

vector_2 - Second vector

Return type
-----------------------------------------------------

array

Example
-----------------------------------------------------

>>> pyvect.bisector([1,4,3],[6,7,2])

Output
------------------------------------------------------

+----------------------------------------------------+
| array([0.83211486, 1.52646306, 0.80034798])        |
+----------------------------------------------------+

pyvect.pos_vector()
=======================================================

About
-------------------------------------------------------

Returns a position vector between any two given vectors.

Syntax
-------------------------------------------------------

>>> pos_vector(vector_1,vector_2)

vector_1 - First vector

vector_2 - Second vector.

Return type
--------------------------------------------------------

array

Example
--------------------------------------------------------

>>> pyvect.pos_vector([1,3,4],[5,7,1])

Output
--------------------------------------------------------

+------------------------------------------------------+
| array([[3. , 5. , 2.5]])                             |
+------------------------------------------------------+

pyvect.iscoplanar()
========================================================

About
--------------------------------------------------------

Returns the boolean value (True) if the given three vectors satisfy the condition.

Syntax
--------------------------------------------------------

>>> iscoplanar(vector_1,vector_2,vector_3)

vector_1 - First vector

vector_2 - Second vector

vector_3 - Third vector.

Return type
--------------------------------------------------------

bool

Example
--------------------------------------------------------

>>> pyvect.iscoplanar([1,4,2],[5,3,8],[1,6,7])

Output
--------------------------------------------------------

+------------------------------------------------------+
| False                                                |
+------------------------------------------------------+

pyvect.reciprocal()
============================================================

About
------------------------------------------------------------

Returns three reciprocal vector for the given three vectors.

Syntax
------------------------------------------------------------

>>> reciprocal(vector_1,vector_2,vector_3)

vector_1 - First vector

vector_2 - Second vector

vector_3 - Third vector.

Return type
-------------------------------------------------------------
array

Example
--------------------------------------------------------------

>>> pyvect.reciprocal([1,4,2],[5,3,8],[1,6,7])

Output
--------------------------------------------------------------

+------------------------------------------------------------+
| array([[[ 0.33333333,  0.33333333, -0.33333333],           |
|       [ 0.19753086, -0.0617284 ,  0.02469136],             |
|       [-0.32098765, -0.02469136,  0.20987654]]])           |
+------------------------------------------------------------+

pyvect.max_value()
==============================================================

About
--------------------------------------------------------------

Returns the maximum value between any two given vectors.

Syntax
-------------------------------------------------------------

>>> max_value(vector_1,vector_2)

vector_1 - First vector

vector_2 - Second vector.

Return type
--------------------------------------------------------------

float

Example
---------------------------------------------------------------

>>> pyvect.max_value([1,4,2],[5,3,8])

Output
---------------------------------------------------------------

+-------------------------------------------------------------+
| 45.36518488885502                                           |
+-------------------------------------------------------------+

pyvect.min_value()
==============================================================

About
--------------------------------------------------------------

Returns the minimum value between any two given vectors.

Syntax
-------------------------------------------------------------

>>> min_value(vector_1,vector_2)

vector_1 - First vector

vector_2 - Second vector.

Return type
--------------------------------------------------------------

float

Example
---------------------------------------------------------------

>>> pyvect.min_value([1,4,2],[5,3,8])

Output
---------------------------------------------------------------

+-------------------------------------------------------------+
| -45.36518488885502                                          |
+-------------------------------------------------------------+


pyvect.area.triangle_adj()
==============================================================

About
--------------------------------------------------------------

Returns the area of a triangle where the two adjacent sides of the triangle are given.

Syntax
-------------------------------------------------------------

>>> triangle_adj(vector_1,vector_2)

vector_1 - First adjacent side 

vector_2 - Second adjacent side

Return type
--------------------------------------------------------------

float

Example
---------------------------------------------------------------

>>> pyvect.area.triangle_adj([1,4,2],[6,4,8])

Output
---------------------------------------------------------------

+-------------------------------------------------------------+
| 15.748015748023622                                          |
+-------------------------------------------------------------+

pyvect.area.triangle_pos()
==============================================================

About
--------------------------------------------------------------

Returns the area of the triangle based on the given three positional vectors.

Syntax
---------------------------------------------------------------

>>> triangle_pos(p1,p2,p3)

p1,p2,p3 - positional vectors of the triangle.

Return type
---------------------------------------------------------------

float

Example
---------------------------------------------------------------

>>> pyvect.area.triangle_pos([2,3,4],[1,5,7],[4,5,1])

Output
---------------------------------------------------------------

+-------------------------------------------------------------+
| 6.87386354243376                                            |
+-------------------------------------------------------------+

pyvect.area.quad()
===============================================================

About
---------------------------------------------------------------

Returns the area of a quadrilateral based on the diagonal vectors.

Syntax
----------------------------------------------------------------

>>> quad(diagonal_1,diagonal_2)

diagonal_1 - Primary diagonal of the quadrilateral

diagonal_2 - Secondary diagonal of the quadrilateral

Return type
-----------------------------------------------------------------

float

Example
-----------------------------------------------------------------

>>> pyvect.area.quad([1,3,5],[2,3,6])

Output
-----------------------------------------------------------------

+---------------------------------------------------------------+
| 2.9154759474226504                                            |
+---------------------------------------------------------------+

pyvect.area.parallelogram()
=================================================================

About
-----------------------------------------------------------------

Returns the area of parallelogram based on the two adjacent vectors.

Syntax
-----------------------------------------------------------------

>>> parallelogram(vector_1,vector_2)

vector_1 - First vector

vector_2 - Second vector

Return type
-----------------------------------------------------------------

float

Example
-----------------------------------------------------------------

>>> pyvect.area.parallelogram([1,4,5],[3,2,7])

Output
------------------------------------------------------------------

+----------------------------------------------------------------+
| 22.090722034374522                                             |
+----------------------------------------------------------------+

pyvect.area.tetrahedron()
==================================================================

About
------------------------------------------------------------------

Returns the area of tetrahedron based on the three position vectors.

Syntax
------------------------------------------------------------------

>>> tetrahedron(p1,p2,p3)

p1,p2,p3 - Positional vectors of the tetrahedron

Return type
--------------------------------------------------------------------

float

Example
--------------------------------------------------------------------

>>> pyvect.area.tetrahedron([1,4,5],[3,2,7],[2,4,1])

Output
--------------------------------------------------------------------

+------------------------------------------------------------------+
| 9.6628                                                           |
+------------------------------------------------------------------+

pyvect.cent.triangle()
=====================================================================

About
---------------------------------------------------------------------

Returns the centroid vector in the triangle based on the the three given positional vectors.

Syntax
---------------------------------------------------------------------

>>> triangle(p1,p2,p3)

p1,p2,p3 - Positional vectors of the triangle

Return type
----------------------------------------------------------------------

array

Example
----------------------------------------------------------------------

>>> pyvect.cent.triangle([1,4,5],[3,2,7],[2,4,1])

Output
----------------------------------------------------------------------

+--------------------------------------------------------------------+
| array([[1.98, 3.3 , 4.29]])                                        |
+--------------------------------------------------------------------+

pyvect.cent.tetrahedron()
=====================================================================

About
---------------------------------------------------------------------

Returns the centroid vector in the tetrahedron based on the the four given positional vectors.

Syntax
---------------------------------------------------------------------

>>> tetrahedron(p1,p2,p3,p4)

p1,p2,p3,p4 - Positional vectors of the tetrahedron

Return type
----------------------------------------------------------------------

array

Example
----------------------------------------------------------------------

>>> pyvect.cent.tetrahedron([1,4,5],[3,2,7],[2,4,1],[3,5,6])

Output
----------------------------------------------------------------------

+--------------------------------------------------------------------+
| array([[2.25, 3.75, 4.75]])                                        |
+--------------------------------------------------------------------+

pyvect.dist.pl_line()
======================================================================

About
----------------------------------------------------------------------

Returns the distance between two parallel lines.

Syntax
-----------------------------------------------------------------------

>>> pl_line(a1_vector,a2_vector,u_vector)

a1_vector, a2_vector - position vectors

u_vector - vector part of arbitrary constants s, t

Return type
-----------------------------------------------------------------------

float

Example
-----------------------------------------------------------------------

>>> pyvect.dist.pl_line([1,2,3],[4,5,6],[7,8,9])

Output
-----------------------------------------------------------------------

+---------------------------------------------------------------------+
| 0.5275893435844943                                                  |
+---------------------------------------------------------------------+

pyvect.dist.sk_line()
=======================================================================

About
-----------------------------------------------------------------------

Returns the distance between two skew lines.

Syntax
-----------------------------------------------------------------------

>>> sk_line(a1_vector,a2_vector,u_vector,v_vector)

a1_vector, a2_vector - position vectors

u_vector - vector part of arbitrary constant t , v_vector - vector part of arbitrary constant s

Return type
------------------------------------------------------------------------

float

Example
------------------------------------------------------------------------

>>> pyvect.dist.sk_line([1,2,3],[2,6,7],[5,2,5],[6,8,1])

Output
-------------------------------------------------------------------------

+-----------------------------------------------------------------------+
| 3.2576045465500365                                                    |
+-----------------------------------------------------------------------+

pyvect.dist.pt_plane()
=========================================================================

About
-------------------------------------------------------------------------

Returns the distance between a point and a plane.

Syntax
-------------------------------------------------------------------------

>>> pt_plane(x_co_ordinate,y_co_ordinate,z_co_ordinate,x_coeff,y_coeff,z_coeff,constant)

x_co_ordinate - x co-ordinate value of the point, y_co_ordinate - y co-ordinate value of the point, z_co_ordinate - z co-ordinate value of the point.

x_coeff - coefficient of x in the plane equation, y_coeff - coefficient of y in the plane equation, z_coeff - coefficient of z in the plane equation.

constant - constant value of plane equation.

Return type
-------------------------------------------------------------------------

float

Example
-------------------------------------------------------------------------

>>> pyvect.dist.pt_plane(1,2,3,4,5,6,7)

Output
-------------------------------------------------------------------------

+-----------------------------------------------------------------------+
| 4.444462481925879                                                     |
+-----------------------------------------------------------------------+

pyvect.dist.or_plane()
=========================================================================

About
-------------------------------------------------------------------------

Returns the distance between origin and a plane.

Syntax
-------------------------------------------------------------------------

>>> or_plane(x_coeff,y_coeff,z_coeff,constant)

x_coeff - coefficient of x in the plane equation, y_coeff - coefficient of y in the plane equation, z_coeff - coefficient of z in the plane equation.

constant - constant value of plane equation.

Return type
-------------------------------------------------------------------------

array

Example
-------------------------------------------------------------------------

>>> pyvect.dist.or_plane(1,2,3,4)

Output
-------------------------------------------------------------------------

+-----------------------------------------------------------------------+
| array([1.06904497])                                                   |
+-----------------------------------------------------------------------+

pyvect.dist.pl_planes()
=========================================================================

About
-------------------------------------------------------------------------

Returns the distance between two parallel planes.

Syntax
-------------------------------------------------------------------------

>>> pl_planes(x_coeff,y_coeff,z_coeff,constant1,constant2)

x_coeff - coefficient of x in the plane equation, y_coeff - coefficient of y in the plane equation, z_coeff - coefficient of z in the plane equation,

constant1 - constant value of first plane.

constant2 - constant value of second plane.

Return type
-------------------------------------------------------------------------

float

Example
-------------------------------------------------------------------------

>>> pyvect.dist.pl_planes(2,3,8,1,6)

Output
-------------------------------------------------------------------------

+-----------------------------------------------------------------------+
| 0.5698028822981898                                                    |
+-----------------------------------------------------------------------+

pyvect.dist.distance()
=========================================================================

About
-------------------------------------------------------------------------

Returns the magnitude of vector.

Syntax
-------------------------------------------------------------------------

>>> distance(x1,x2,y1,y2,z1,z2)

x1 - x_co_ordinate of first vector, x2 - x_co_ordinate of second vector

y1 - y_co_ordinate of first vector, y2 - x_co_ordinate of second vector

z1 - z_co_ordinate of first vector, z2 - z_co_ordinate of second vector

Return type
-------------------------------------------------------------------------

float

Example
-------------------------------------------------------------------------

>>> pyvect.dist.distance(2,6,4,7,8,0)

Output
-------------------------------------------------------------------------

+-----------------------------------------------------------------------+
| 9.433981132056603                                                     |
+-----------------------------------------------------------------------+

pyvect.prod.s3()
=========================================================================

About
-------------------------------------------------------------------------

Returns the scalar triple product of the given three vectors.

Syntax
-------------------------------------------------------------------------

>>> s3(vector_1,vector_2,vector_3)

vector_1 - First vector

vector_2 - Second vector 

vector_3 - Third vector

Return type
-------------------------------------------------------------------------

int

Example
-------------------------------------------------------------------------

>>> pyvect.prod.s3([7,9,6],[6,8,5],[3,5,4])

Output
-------------------------------------------------------------------------

+-----------------------------------------------------------------------+
| 4                                                                     |
+-----------------------------------------------------------------------+

pyvect.prod.s4()
=========================================================================

About
-------------------------------------------------------------------------

Returns the scalar product of the given four vectors.

Syntax
-------------------------------------------------------------------------

>>> s4(vector_1,vector_2,vector_3,vector_4)

vector_1 - First vector

vector_2 - Second vector 

vector_3 - Third vector

vector_4 - Fourth vector

Return type
-------------------------------------------------------------------------

int

Example
-------------------------------------------------------------------------

>>> pyvect.prod.s4([7,9,6],[6,8,5],[3,5,4],[2,3,1])

Output
-------------------------------------------------------------------------

+-----------------------------------------------------------------------+
| 24                                                                    |
+-----------------------------------------------------------------------+

pyvect.prod.v3()
=========================================================================

About
-------------------------------------------------------------------------

Returns the vector triple product of the given three vectors.

Syntax
-------------------------------------------------------------------------

>>> pyvect.prod.v3(vector_1,vector_2,vector_3)

vector_1 - First vector

vector_2 - Second vector 

vector_3 - Third vector

Return type
-------------------------------------------------------------------------

array

Example
-------------------------------------------------------------------------

>>> pyvect.prod.v3([7,9,6],[6,8,5],[3,5,4])

Output
-------------------------------------------------------------------------

+-----------------------------------------------------------------------+
| [-6 18 -18]                                                           |
+-----------------------------------------------------------------------+

pyvect.prod.v4()
=========================================================================

About
-------------------------------------------------------------------------

Returns the vector product of given four vectors.

Syntax
-------------------------------------------------------------------------

>>> v4(vector_1,vector_2,vector_3,vector_4)

vector_1 - First vector

vector_2 - Second vector

vector_3 - Third vector

vector_4 - Fourth vector

Return type
--------------------------------------------------------------------------

array

Example
--------------------------------------------------------------------------

>>> pyvect.prod.v4([1,2,3],[4,5,6],[7,8,9],[1,5,10])

Output
--------------------------------------------------------------------------

+------------------------------------------------------------------------+
| array([[[-21, -24, -27]]])                                             |
+------------------------------------------------------------------------+

pyvect.section.internal()
==========================================================================

About
--------------------------------------------------------------------------

Returns a vector using section formula using internal method

Syntax
--------------------------------------------------------------------------

>>> internal(p_vector1,p_vector2,m,n)

p_vector1, p_vector2 - Positional vectors

m, n - Parameters of the ratio (m:n)

Return type
--------------------------------------------------------------------------

array

Example
--------------------------------------------------------------------------

>>> pyvect.section.internal([1,2,3],[4,5,6],3,2)

Output
--------------------------------------------------------------------------

+------------------------------------------------------------------------+
| array([[-5., -4., -3.]])                                               |
+------------------------------------------------------------------------+

pyvect.section.external()
==========================================================================

About
--------------------------------------------------------------------------

Returns a vector using section formula using external method

Syntax
--------------------------------------------------------------------------

>>> external(p_vector1,p_vector2,m,n)

p_vector1, p_vector2 - Positional vectors

m, n - Parameters of the ratio (m:n)

Return type
--------------------------------------------------------------------------

array

Example
--------------------------------------------------------------------------

>>> pyvect.section.external([1,2,3],[4,5,6],3,2)

Output
--------------------------------------------------------------------------

+------------------------------------------------------------------------+
| array([[ 4.6,  8. , 11.4]])                                            |
+------------------------------------------------------------------------+

pyvect.volume.parallelopiped()
==========================================================================

About
--------------------------------------------------------------------------

Returns the volume of the parallelopiped formed by three vectors.

Syntax
--------------------------------------------------------------------------

>>> parallelopiped(vector_1,vector_2,vector_3)

vector_1, vector_2, vector_3 - Respective first, second and third vectors.

Return type
--------------------------------------------------------------------------

int

Example
--------------------------------------------------------------------------

>>> pyvect.volume.parallelopiped([9,3,6],[4,5,6],[7,8,9])

Output
--------------------------------------------------------------------------

+------------------------------------------------------------------------+
| 27                                                                     |
+------------------------------------------------------------------------+

