
from __future__ import absolute_import
from setuptools import setup, find_packages
from graphication import release

setup(
    zip_safe=False,
    name=release.product,
    version=release.version,
    packages=find_packages(include=('graphication*',)),
    package_data={'graphication': ['*.css']},
    install_requires=[
        'six',
        'pycairo>=1.17.0',
    ],
    extras_require={'dev': [
        'pytest>=3.6.0',
        'pytest-cov>=2.5.1',
    ]},
    description="A Cairo-based graphing library",
    author="Andrew Godwin",
    author_email="graphication@aeracode.org",
    url="http://aeracode.org/projects/graphication/",
    license="GPL",
)
