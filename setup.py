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
    long_description="An implementation of the “BellKor’s Pragmatic Chaos”'s final solution",
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
    install_requires=[
        "pandas==1.0.3",
        "pytest==5.4.1",
        "notebook==6.4.1",
        "numpy==1.18.2",
        "ipython==7.16.3",
    ],
    tests_require=["pytest==5.4.1"],
)
