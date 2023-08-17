
#Build entire machine learning project as a package and deploy to a package manager
#Like pom.xml in maven

from setuptools import find_packages, setup
from typing import List

EXCLUDE='-e .'

def get_requirements(file_path: str) ->List[str]:
    '''
    This function returns list of requirements
    '''
    requirements=[]
    with open (file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements= [req.replace("\n", "" ) for req in requirements]
    if EXCLUDE in requirements:
        requirements.remove(EXCLUDE)
    
    return requirements


setup(
    name= 'mlproject',
    version='0.0.1',
    author='Rohit',
    author_email='rohit.tew@gmail.com',
    packages=find_packages(),
    install_requires= get_requirements('requirements.txt')
)