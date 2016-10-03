#!/usr/bin/env python
# coding=utf-8

import os
from setuptools import setup

package_name = 'tsv2tr'
filename = package_name + '.py'

# Read file
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

def get_version():
    import ast

    with open(filename) as input_file:
        for line in input_file:
            if line.startswith('__version__'):
                return ast.parse(line).body[0].value.s

def get_long_description():
    try:
        with open('README.md', 'r') as f:
            return f.read()
    except IOError:
        return ''


setup(
    name=package_name,
    version=get_version(),
    description='convert from tab-separated to HTML <tr> format',
    author='njhammond',
    author_email='njhammond_github@hammondsoftware.com',
    url='https://github.com/njhammond/tsv2tr',
    long_description=get_long_description(),
    py_modules=[package_name],
    entry_points={
        'console_scripts': [
            'tsv2tr = tsv2tr:main'
        ]
    },
    license='License :: OSI Approved :: MIT License',
)
