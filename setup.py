#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" Python Setup File
"""
from setuptools import find_packages
from setuptools import setup

setup(
    # Module Name.
    name="BellKor",
    # Versions should comply with PEP440.
    version="0.1.0",
    # Module Short and Long Descriptions.
    description="Bellkor Algorithm",
    long_description="Running example of the Bellkor Algorithm, uses NumPy.",
    # The project"s main homepage.
    url="",
    # Author Details.
    author="Dan Dixey",
    author_email="dan@functorml.co.uk",
    # Need to update to credit Wood Mackenzie"s License
    license="",
    # Project Classifiers
    classifiers=[
        # How mature is this project? Common values are
        "Development Status :: 4 - Beta",
        # Indicate who your project is intended for
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        # Language
        "Natural Language :: English",
        # Programming Language
        "Programming Language :: Python",
        # Specify the Python versions you support here.
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
    ],
    # What does your project relate to?
    keywords="Netflix, Bellkor",
    # Find all the Projects packages
    packages=find_packages(),
    install_requires=["pandas==0.23.3",
                      "notebook>5.7.2",
                      "ipython>6.2.1"],
    # List additional groups of dependencies here (e.g. development dependencies).
    extras_require={
        "developer": ["bumpversion==0.5.3"],
        "test": ["pytest>3.3.2"],
        "docs": ["sphinx==1.6.3", "sphinx_rtd_theme"]
    },
    tests_require=["pytest"]
)
