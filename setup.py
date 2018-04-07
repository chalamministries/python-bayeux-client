#!/usr/bin/env python
from setuptools import setup

version = '1.5'

setup(name='python-bayeux-client',
      version=version,
      description='A simple python bayeux client',
      author='David Madigan',
      author_email='dkmadigan@gmail.com',
      url='http://github.com/chalamministries/python-bayeux-client',
      license="LICENSE.txt",
      long_description=open('README.md').read(),
      packages=['bayeux']
     )