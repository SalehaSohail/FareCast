"""
This script (setup.py) makes the project installable as a proper Python
package. This is necessary if the project is to be installed via pip,
and it also makes it possible to import our own modules cleanly across
the project.

A helper function reads the required libraries from requirements.txt
instead of listing them manually inside install_requires. Hardcoding
each dependency by hand would be inefficient and error-prone, especially
as the project grows and dependencies change.

List comprehension is used to strip whitespace and special characters
from each line read from the file. This is a more concise and efficient
approach than writing a separate for loop to iterate over each item and
strip it individually.
"""


from setuptools import find_packages,setup
from typing import List

requirements_file_name="requirements.txt"
REMOVE_PACKAGE="-e ."

def get_requirements()->List[str]:
    with open(requirements_file_name) as requirement_file:
        requirement_list=requirement_file.readlines()
    requirement_list = [requirement_name.strip() for requirement_name in requirement_list]


    if REMOVE_PACKAGE in requirement_list:
        requirement_list.remove(REMOVE_PACKAGE)

    return requirement_list


setup(
    name="Flight Fare",
    version="0.0.1",
    description="Industry standard project modular based",
    author="Saleha Sohail",
    author_email="saleha.sohail064@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements()
)