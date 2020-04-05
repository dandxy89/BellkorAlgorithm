#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
"""
from setuptools import find_packages, setup

from Bellkor import __version__, __developers__

setup(
    name="BellKor",
    version=__version__,
    description="Bellkor Algorithm",
    long_description="Running example of the Bellkor Algorithm, uses NumPy.",
    url="",
    author=__developers__,
    author_email="dan@functorml.co.uk",
    license="",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "Natural Language :: English",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    keywords=["Netflix", "Bellkor"],
    packages=find_packages(),
    install_requires=["pandas==0.23.3",
                      "pytest>3.3.2",
                      "notebook>5.7.2",
                      "ipython>6.2.1"],
    tests_require=["pytest>3.3.2"]
)
