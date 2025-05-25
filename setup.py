from setuptools import find_packages, setup
import os

def get_requirements(file_path):
    requirements = []
    if os.path.exists(file_path):
        with open(file_path, "r") as file_obj:
            requirements = [
                req.strip()
                for req in file_obj.readlines()
                if req.strip() and req.strip() != "-e ."
            ]
    return requirements

setup(
    name="mlproject",
    version="0.1",
    author="Irfan",
    author_email="if476771@gmail.com",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=get_requirements('requirements.txt'),
)