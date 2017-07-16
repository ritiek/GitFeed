#!/usr/bin/python

from setuptools import setup, find_packages
import gitfeed

with open("README.rst", "r") as f:
    long_description = f.read()

setup(name='GitFeed',
      version=gitfeed.__version__,
      description='Check your GitHub Newsfeed via the command-line.',
      long_description=long_description,
      author='Ritiek Malhotra',
      author_email='ritiekmalhotra123@gmail.com',
      packages = find_packages(),
      entry_points={
            'console_scripts': [
                  'gitfeed = gitfeed.gitfeed:cli',
            ]
      },
      url='https://www.github.com/ritiek/GitFeed',
      keywords=['GitHub', 'news', 'feed', 'command-line', 'python'],
      license='MIT',
      download_url='https://github.com/Ritiek/GitFeed/archive/v' + gitfeed.__version__ + '.tar.gz',
      classifiers=[],
      install_requires=[
            'requests >= 2.17.3',
            'colorama >= 0.3.7',
      ]
     )

