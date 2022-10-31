from setuptools import find_packages,setup
from typing import List
def get_requirements()->List[str]:
    """
    this function returns list of requirements
    """
    requirement_list:List[str] = []
    return requirement_list

setup(
    
    name="sensor",
    version="0.0.1",
    author="Arunteja",
    author_email="arunteja.lonka@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements(),

)