from setuptools import find_packages, setup
from typing import List

HYPHEN_E_DOT = "-e ."

def get_requirements(file_path:str)-> List[str]:
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]
        if HYPHEN_E_DOT in requirements:
                requirements.remove(HYPHEN_E_DOT)
    return requirements

setup(
    name = "UserBehaviour Analysis for Powr Of You",
    version = "1.0.0",
    author = "Krishnaprakash",
    author_email = "krishnaprakash997#gmail.com",
    packages = find_packages(),
    install_requires = get_requirements('requirements.txt')
    )