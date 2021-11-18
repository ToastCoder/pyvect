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
        print(f'Memory usage:\t\t {current / 10**6:.6f} MB \n'
              f'Peak memory usage:\t {peak / 10**6:.6f} MB ')
        print(f'Time elapsed in seconds: {finish_time - start_time:.6f} s')
        print(f'{"-"*40}')

        tracemalloc.stop()

        return func(*args, **kwargs)

    return wrapper

# Tester function for pyvect.dot()
@perf_tester
def dot_tester(a:List[int], b:List[int]) -> str:
    '''Tests the dot product function'''
    return f"Dot Product: {pyvect.dot(a,b)}"

# Main function
if __name__ == '__main__':
    print(dot_tester([1,2,3],[4,5,6]))






