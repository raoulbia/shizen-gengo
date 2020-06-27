# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

import shizen_gengo

VERSION = shizen_gengo.__version__
NAME = 'shizen gengo'
DESCRIPTION = 'A set of python functions for common hand-on NLP tasks'

with open('README.md') as f:
    LONG_DESCRIPTION = f.read()

AUTHOR = 'Raoul Biagioni'
URL = 'https://raoulbia.github.io/'

with open('LICENSE') as f:
    LICENSE = f.read()

setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    author=AUTHOR,
    url=URL,
    install_requires=['pytest'
                      'nltk',
                      'pandas',
                      'numpy',
                      'jupyterlab'
                      ],
    license=LICENSE,
    packages=find_packages(exclude=('tests', 'docs')),
    extras_require={}
)
