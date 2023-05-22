"""This module defines setup procedure.
"""
import os
from setuptools import setup, find_packages

pkg_name = "template-python-project"

# Get version
exec(open(os.path.join(pkg_name, "version.py")).read())

setup(
    name=pkg_name,
    version=__version__,
    url="https://github.com/korjaa/template-python-project",
    author="Jaakko Korhonen",
    author_email="user@email.com",
    description="Template project for Python projects with CLI binding.",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            f"{pkg_name}={pkg_name}.cli:main"
        ]
    },
    install_requires=[
        "requests == 2.31.0"
    ],
)
