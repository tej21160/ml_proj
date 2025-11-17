from setuptools import find_packages,setup
from typing import List


hype= "-e ."
def get_requirements(file_path:str)->List[str]:
    '''
    This func will return the list of requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n","") for req in requirements]

        if hype in requirements:
            requirements.remove(hype)
    return requirements


setup(
name='ML_Project',
version='0.0.1',
author='Kumar Tejas',
author_email='gottabetej@gmail.com',
packages=find_packages(),
install_requires=get_requirements('requirements.txt')

)