# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

import shizen_gengo

VERSION = shizen_gengo.__version__
NAME = 'shizen gengo'
DESCRIPTION = 'A set of python functions for common hand-on NLP tasks'

with open('README.md') as f:
    LONG_DESCRIPTION = f.read()

AUTHOR = 'Raoul Biagioni'
URL = 'https://github.com/raoulbia/shizen_gengo.git'
DOWNLOAD_URL = 'https://github.com/raoulbia/shizen_gengo/archive/0.1.0.tar.gz'

with open('LICENSE') as f:
    LICENSE = f.read()

setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    author=AUTHOR,
    url=URL,
    download_url = DOWNLOAD_URL,
    install_requires=['nltk',
                      'pandas',
                      'numpy'
                      ],
    license=LICENSE,
    packages=find_packages(exclude=('tests', 'docs')),
    extras_require={'docs': ['recommonmark',
                             'sphinx',
                             'sphinx_rtd_theme',
                             'sphinxcontrib.bibtex'],
                    'tests':['pytest']
                    }
)
