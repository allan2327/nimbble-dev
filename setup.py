#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

import nimbble
version = nimbble.__version__

setup(
    name='nimbble',
    version=version,
    author='',
    author_email='Your email',
    packages=[
        'nimbble',
    ],
    include_package_data=True,
    install_requires=[
        'Django>=1.7.1',
    ],
    zip_safe=False,
    scripts=['nimbble/manage.py'],
)
