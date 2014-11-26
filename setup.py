#!/usr/bin/env python

from setuptools import setup

setup(name='change_org',
      version='1.0',
      description='Python interface for the change.org REST API',
      author='Rukmal Weerawarana',
      author_email='rukmal.weerawarana@gmail.com',
      url='http://github.com/AGISR/Change.org-Python-API',
      packages=['change_org'],
      tests_require=['pytest']
     )