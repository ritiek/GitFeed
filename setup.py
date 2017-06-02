#!/usr/bin/python

from setuptools import setup, find_packages
import gitfeed

setup(name='GitHub-Newsfeed',
      version='0.1.0',
      description='GitHub Newsfeed right in your terminal',
      author='Ritiek Malhotra',
      author_email='ritiekmalhotra123@gmail.com',
      packages = find_packages(),
      entry_points={
            'console_scripts': [
                  'gitfeed = gitfeed.gitfeed:cli',
            ]
      },
      url='https://www.github.com/Ritiek/GitHub-Newsfeed',
      keywords=['GitHub', 'newsfeed', 'command-line', 'python'],
      license='MIT',
      download_url='https://github.com/Ritiek/GitHub-Newsfeed/archive/v0.1.0.tar.gz',
      classifiers=[],
      install_requires=[
            'requests',
            'colorama',
      ]
     )

