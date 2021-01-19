import os
from codecs import open

from setuptools import setup

with open(os.path.join(os.path.dirname(__file__), "README.md")) as f:
    long_description = f.read()

setup(
  name = 'pyvect',         
  packages = ['pyvect'],
  version = '1.0.2',
  license='MIT',
  description = 'Pyvect is a open source python module created for the purpose of simplifying the vector calculations such as finding the angle between vectors, projection of one vector over the other and much more...!',
  long_description = long_description,
  long_description_content_type = "text/markdown",
  author = ['Vigneshwar K R','Mouli Shankar M R','Vishal Balaji Sivaraman'],
  author_email = 'vicky.pcbasic@gmail.com',
  url = 'https://github.com/ToastCoder/pyvect',
  download_url = 'https://github.com/ToastCoder/pyvect/archive/master.zip',
  keywords = ['VECTOR', 'VECTOR_ALGEBRA_FUNCTIONS','VECTOR_CALCULATIONS'],
  install_requires=['numpy'],
  classifiers=[
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',      
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
  ],
)

