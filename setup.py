'''
The setup.py file is an essential part of packaging and 
distributing Python projects. It is used by setuptools 
(or distutils in older Python versions) to define the configuration 
of your project, such as its metadata, dependencies, and more
'''

from setuptools import setup, find_packages
from typing import List

def get_requirements() -> List[str]:
    """

    This function returns a list of requirements for the project.

    """
    requirement_lst: List[str] = []
    try:
        with open('requirements.txt','r') as f:
            ## Read lines from the file
            lines = f.readlines()
            ## Process each line 
            for line in lines:
                requirement = line.strip()
                ## Ignore empty lines and -e . 
                if requirement and requirement != '-e .':
                    requirement_lst.append(requirement)
    except FileNotFoundError:
        print("reqirements.txt file not found. please ensure it exists.")

    return requirement_lst

setup(
    name = 'NetworkSecurity',
    version= '0.0.1',
    author= 'Ahmed Elgayar',
    author_email= 'a.elgayar17@gmail.com',
    packages= find_packages(),
    install_requires = get_requirements()
)