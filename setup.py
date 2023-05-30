#!/usr/bin/python

from setuptools import setup

setup( \
    name='bquery',
    version='0.1',
    description='bQuery is a simple tool to quickly parse html streams with a jQuery-like expression',
    author='mont5piques',
    author_email='newishak@gmail.com',
    license = "WTFPL",
    url='http://github.com/mont5piques/bquery',
    scripts=['bquery'],
    install_requires=['pyquery>=1.2'],
)

# ok faisons ça
# faisons-ci