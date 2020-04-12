"""This module defines setup procedure.
"""
from setuptools import setup, find_packages

setup(
    name="template-python-project",
    version="0.1.0",
    url="https://github.com/korjaa/template-python-project",
    author="Jaakko Korhonen",
    author_email="user@email.com",
    description="Template project for Python projects with CLI binding.",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "template-python-project=template_python_project.cli:main"
        ]
    },
    install_requires=[
        "requests == 2.22.0"
    ],
)
