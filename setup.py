from setuptools import setup, find_packages
from typing import List
HYPHEN_E_DOT = "-e ."

def get_requirements(file_path: str) -> List[str]:
    '''Reads a requirements file and returns a list of packages.'''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", " ") for req in requirements]
        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
    return requirements

setup(
    name="mlProject",
    version="0.0.1",
    author="Vishal Kumar",
    author_email="vishalk190597@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt"),
)
