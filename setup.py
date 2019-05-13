#!/usr/bin/env python

import os
from setuptools import setup
from setuptools import find_packages

PACKAGES = ['uploadfundrequest'] + list(map(lambda s: 'uploadfundrequest.' +
                                                     s, find_packages('uploadfundrequest')))

# packages not part of the stdlib
SETUP_REQUIRES = [

]

INSTALL_REQUIRES = []
DEPENDENCY_LINKS = []

if os.environ.get('IMAGE_NAME', None) is None:
    INSTALL_REQUIRES = [

    ]

    DEPENDENCY_LINKS = [
    ]

TESTS_REQUIRE = [

]

PACKAGE_DATA = {}

# load package version information
about = {}

cwd = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(cwd, 'uploadfundrequest', '__version__.py'), 'r') as f:
    exec(f.read(), about)

# assume availability of setuptools
setup(
    name=about['__title__'],
    version=about['__version__'],
    description=about['__description__'],
    author=about['__author__'],
    author_email=about['__author_email__'],
    url=about['__url__'],
    license=about['__license__'],
    python_requires=">=3.6.*",
    package_dir={'uploadfundrequest': 'uploadfundrequest'},
    packages=PACKAGES,
    package_data=PACKAGE_DATA,
    setup_requires=SETUP_REQUIRES,
    install_requires=INSTALL_REQUIRES,
    dependency_links=DEPENDENCY_LINKS,
    tests_require=TESTS_REQUIRE,
    entry_points={
        'console_scripts': [
            'uploadfr=uploadfundrequest.__main__:main'
        ]
    },
    zip_safe=False
)
