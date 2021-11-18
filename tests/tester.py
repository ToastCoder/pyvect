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

# Importing the library for testing
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir) 
import pyvect as pv


