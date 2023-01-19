#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name="computepac",
    version="1.5",
    description="A Python package for numerical analysis: root finding, iterative solvers, other algorithms.",
    url="https://github.com/mathemacode/computepac",
    author="glider4",
    classifiers=["License :: GNU GPLv3" "Programming Language :: Python 3.7"],
    keywords="computational mathematics engineering numerical analysis finite difference iterative schemes root finding algorithms",
    package_dir={"": "computepac"},
    packages=find_packages(where="computepac"),
    python_requires=">3.5",
    install_requires=["scipy", "numpy", "sympy", "pytest"],
)
