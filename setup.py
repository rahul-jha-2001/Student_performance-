from setuptools import find_packages,setup
from typing import List
HYPE_E_DOT = "-e ."
def get_req(path_file:str)->List(str):
    requirements = []
    with open(path_file) as file_obj:
        requirements = file_obj.readlines
        requirements = [req.replace("\n","") for req in requirements]
        if HYPE_E_DOT in requirements:
            requirements.remove(HYPE_E_DOT)
    return requirements        

setup(
 name =  "ml_project",
 version= "0.0.1",
 author = "rahul",
 packages= find_packages(),
 install_requires =  get_req("requirement.txt")
)