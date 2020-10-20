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

Output
---------------------------------------

+-------------------------------------+
| 2.0943951023931953                  |
+-------------------------------------+

vectoralg.projection()
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

>>> vectoralg.projection([1,2,3],[4,5,6])

Output
----------------------------------------

+--------------------------------------+
| 3.6467384467084143                   |
+--------------------------------------+

vectoralg.isperpendicular()
========================================

About
-----------------------------------------

Returns True if two vectors are perpendicular to each other. (i.e) Dot product of the two vectors is zero.

Syntax
-----------------------------------------

>>> vectoralg.isperpendicular(vector_1,vector_2)

vector_1 - First vector

vector_2 - Second vector

Return type
------------------------------------------

bool

Example
------------------------------------------

>>> vectoralg.isperpendicular([-3,4,-7],[2,-51,-30])

Output
-------------------------------------------

+-----------------------------------------+
| True                                    |
+-----------------------------------------+

vectoralg.iscollinear()
============================================

About
--------------------------------------------

Returns True if two vectors are collinear. (i.e) Cross product of the two vectors is zero.

Syntax
----------------------------------------------

>>> vectoralg.iscollinear(vector_1,vector_2)

vector_1 - First vector

vector_2 - Second vector

Return type
------------------------------------------------
bool

Example
------------------------------------------------

>>> vectoralg.iscollinear([1,2,3],[2,4,6])

Output
-------------------------------------------------

+------------------------------------------------+
| True                                           |
+------------------------------------------------+

vectoralg.unit_vector()
==================================================

About
--------------------------------------------------

Returns the unit vector of the given vector.

Syntax
--------------------------------------------------

>>> vectoralg.unit_vector(vector_1)

vector_1 - Vector provided to the function

Return type
---------------------------------------------------

array

Example
---------------------------------------------------

>>> vectoralg.unit_vector([2,3,7])

Output
---------------------------------------------------

+-------------------------------------------------+
| array([0.25400025, 0.38100038, 0.88900089])     |
+-------------------------------------------------+

vectoralg.unit_normal()
==================================================

About
--------------------------------------------------

Returns the unit normal vector of given two vectors

Syntax
--------------------------------------------------

>>> vectoralg.unit_normal(vector1,vector2)

vector_1 - First vector 

vector_2 - Second vector

Return type
---------------------------------------------------

array

Example
---------------------------------------------------

>>> unit_normal([2,1,1],[1,2,1])

Output
---------------------------------------------------

+--------------------------------------------------------------------------------------------------+
| [array([-0.30151134, -0.30151134,  0.90453403]), array([ 0.30151134,  0.30151134, -0.90453403])] | 
+--------------------------------------------------------------------------------------------------+

vectoralg.bisector()
==================================================

About
---------------------------------------------------

Returns a vector in the direction of the bisector of the angle between two vectors.

Syntax
----------------------------------------------------

>>> vectoralg.bisector(vector_1,vector_2)

vector_1 - First vector

vector_2 - Second vector

Return type
-----------------------------------------------------

array

Example
-----------------------------------------------------

>>> vectoralg.bisector([1,4,3],[6,7,2])

Output
------------------------------------------------------

+----------------------------------------------------+
| array([0.83211486, 1.52646306, 0.80034798])        |
+----------------------------------------------------+

vectoralg.pos_vector()
=======================================================

About
-------------------------------------------------------

Returns a position vector between any two given vectors.

Syntax
-------------------------------------------------------

>>> vectoralg.pos_vector(vector_1,vector_2)

vector_1 - First vector

vector_2 - Second vector.

Return type
--------------------------------------------------------

array

Example
--------------------------------------------------------

vectoralg.pos_vector([1,3,4],[5,7,1])

