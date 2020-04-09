# -*- coding: UTF-8 -*-
""""
Created on 23.12.19

:author:     Martin Dočekal
"""
from setuptools import setup, find_packages

with open('README.md') as readme_file:
    README = readme_file.read()

setup_args = dict(
    name='windPyTorchUtils',
    version='1.0.0',
    description='Useful tools for PyTorch projects.',
    long_description_content_type="text/markdown",
    long_description=README,
    license='The Unlicense',
    packages=find_packages(),
    author='Martin Dočekal',
    keywords=['utils', 'PyTorch', 'PyTorch utils' 'general usage'],
    url='https://github.com/windionleaf/windPyTorchUtils',
    install_requires=[
        'torch>=1.3.1'
    ]
)

if __name__ == '__main__':
    setup(**setup_args)