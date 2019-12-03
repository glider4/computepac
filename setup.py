#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name='compute-pac',
    version='1.0',
    description='A Python package of mathematical functions, iterative solvers, numerical analysis, and more.',
    url='https://github.com/mathemacode/compute-pac',
    author='mathemacode',
    classifiers=[
        'License :: GNU GPLv3'
        'Programming Language :: Python 3.7'
    ],
    keywords='computational mathematics engineering numerical analysis finite difference iterative schemes',
    package_dir={'': 'compute-pac'},
    packages=find_packages(where='compute-pac'),
    python_requires='>3.5',
    install_requires=[
        'numpy',
        'sympy',
        'pytest'
    ],

)
