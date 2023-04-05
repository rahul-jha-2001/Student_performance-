from setuptools import find_packages,setup
HYPE_E_DOT =  '-e .'
def get_req(path_file:str):
    requirements = []
    with open(path_file) as file_obj:
        requirements =  file_obj.readlines()
        requirements =  [req.replace("\n","") for req in requirements]
        
        if HYPE_E_DOT in requirements:
            requirements.remove(HYPE_E_DOT)
    return requirements        

setup(
    name = "ml_project",
    author=  "tahul",
    version= "0.0.1",
    packages= find_packages(),
    install_require =  get_req("requirements.txt")
        )