#!/usr/bin/env python

from setuptools import setup


setup(name='apiary',
      version='0.0.1',
      description='Python version of the Ruby Apiary client',
      author='James Birmingham',
      author_email='james@dimsum.tv',
      packages=['apiary', 'apiary.command'],
      entry_points={
          "console_scripts": [
              "apiary = apiary.__main__:main"
          ]
      })