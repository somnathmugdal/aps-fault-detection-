# Importing required Libraries
from setuptools import find_packages,setup
from typing import List

#Variables
Requirement_File = "requirements.txt"
HyphenEDot = '-e.' # It's Very imp to add into the requirements.txt to trigger

#Function to read requirements.txt(All required pacakages for the project)
def get_requirements() -> List[str]:
    with open(Requirement_File) as requirements_file :
        requirements_list = requirements_file.readlines()
        requirements_list = [requirement_name.replace("\n", "" )for requirement_name in requirements_list]

# Removing "-e." from the requirements_list because its not a package        
    if HyphenEDot in requirements_list :
        requirements_list.remove(HyphenEDot)
    return requirements_list

#Setup parameters   
setup (
    name ="sensor",
    version= "0.0.1",
    author= "Somnath",
    author_email= "svmsomnathsvm@gmail.com",
    packages= find_packages(),
    install_requires = get_requirements(),
)