from setuptools import find_packages, setup
from typing import List

HYPHEN_E_DOT = '-e .'

def get_requirements(file_path: str) -> List[str]:
    '''This function returns the list of requirements.'''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]

        # Remove '-e .' so setuptools doesn't get stuck in a loop
        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)

    return requirements


setup(
    name='1MLproject end to end',
    version='0.0.1',
    author='umar',
    author_email='01umarfaruq12@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')  # Added quotes around 'requirements.txt'
)