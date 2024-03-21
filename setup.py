from setuptools import find_packages, setup
from typing import List

HYPHEN_E_DOT = "-e ."

def get_requirements(filepath:str)-> List[str]:
    """
    This function will return a list of requirements
    """
    with open(filepath) as file_obj:
        requirements = []
        requirements = file_obj.readlines()
        requirements = [requirement.replace("\n", "") for requirement in requirements]
        
        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
        
    return requirements



setup(
    name = "netflix-movies",
    version="0.0.1",
    author="Terry",
    author_email="ratombosoaterryfloriano86@gmail.com",
    packages= find_packages(),
    install_requires = get_requirements("requirements.txt")
)
