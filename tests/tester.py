# Module name: Pyvect
# Short description: Pyvect is a open source python module created for the purpose of simplifying the vector calculations such as finding the angle between vectors, projection of one vector over the other and much more...!
# Developers: Vigneshwar Ravichandar(@ToastCoder), Moulishankar M R (@Moulishankar10), Vishal Balaji Sivaraman (@The-SocialLion) 
# Contact email address: vicky.pcbasic@gmail.com, moulishankarmr@gmail.com, vishalsivaraman5@gmail.com
# Modules required: numpy

# Command to install pyvect:
# >>> pip install pyvect

# File name: tests/tester.py

#---------------------------------------------------------------------------------------------------------------------------------------------------

# Essential modules
import numpy as np
import os
import sys
import inspect
from functools import wraps
import tracemalloc
from time import perf_counter
from typing import List

# Importing the library for testing
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir) 
import pyvect

# Function to calculate the performance of the function
def perf_tester(func):
    '''Measures peformance of a function'''

    @wraps(func)
    def wrapper(*args, **kwargs):
        tracemalloc.start()
        
        start_time = perf_counter()
        func(*args, **kwargs)
        current, peak = tracemalloc.get_traced_memory()
        finish_time = perf_counter()

        print(f'Function Name: {func.__name__}')
        print(f'Description: {func.__doc__}')
        print(f'Memory usage:\t\t {current / 10**3:.6f} KB \n'
              f'Peak memory usage:\t {peak / 10**3:.6f} KB ')
        print(f'Time elapsed in seconds: {finish_time - start_time:.6f} s')
        

        tracemalloc.stop()
        
        return func(*args, **kwargs)
        

    return wrapper

# Tester function for pyvect.dot()
@perf_tester
def dot_tester(x:List[int], y:List[int]) -> str:
    '''Tests the dot product function'''
    return f"Dot Product: {pyvect.dot(x,y)}"

# Tester function for pyvect.cross()
@perf_tester
def cross_tester(x:List[int], y:List[int]) -> str:
    '''Tests the cross product function'''
    return f"Cross Product: {pyvect.cross(x,y)}"

# Tester function for pyvect.angle()
@perf_tester
def angle_tester(x:List[int], y:List[int]) -> str:
    '''Tests the angle function'''
    return f"Angle: {pyvect.angle(x,y)}"

# Tester function for pyvect.projection()
@perf_tester
def projection_tester(x:List[int], y:List[int]) -> str:
    '''Tests the projection function'''
    return f"Projection: {pyvect.projection(x,y)}"

# Tester function for pyvect.modVector()
@perf_tester
def modVector_tester(x:List[int]) -> str:
    '''Tests the modVector function'''
    return f"ModVector: {pyvect.modVector(x)}"

# Tester function for isperpendicular()
@perf_tester
def isperpendicular_tester(x:List[int], y:List[int]) -> str:
    '''Tests the isperpendicular function'''
    return f"isperpendicular: {pyvect.isperpendicular(x,y)}"

# Main function
if __name__ == '__main__':

    a1 = [10,2,4]
    a2 = [4,2,6]
    a3 = [-7,-6,-9]
    a4 = [4,20,12]
    a5 = [1,0,0]
    b1 = [1,2,-2,9]
    b2 = [2,4,-4,-6]
    u = 15
    v = 11

    print(dot_tester(a4,a3))
    print(f'{"-"*40}')

    print(cross_tester(a1,a2))
    print(f'{"-"*40}')

    print(angle_tester(a1,a2))
    print(f'{"-"*40}')

    print(projection_tester(a2,a3))
    print(f'{"-"*40}')

    print(modVector_tester(a3))
    print(f'{"-"*40}')

    print(isperpendicular_tester(a2,a4))
    print(f'{"-"*40}')
