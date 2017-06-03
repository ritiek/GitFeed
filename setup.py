#!/usr/bin/python

from setuptools import setup, find_packages
import gitfeed

setup(name='GitFeed',
      version='0.1.3',
      description='Check your GitHub Newsfeed via the command-line.',
      author='Ritiek Malhotra',
      author_email='ritiekmalhotra123@gmail.com',
      packages = find_packages(),
      entry_points={
            'console_scripts': [
                  'gitfeed = gitfeed.gitfeed:cli',
            ]
      },
      url='https://www.github.com/Ritiek/GitFeed',
      keywords=['GitHub', 'news', 'feed', 'command-line', 'python'],
      license='MIT',
      download_url='https://github.com/Ritiek/GitFeed/archive/v0.1.3.tar.gz',
      classifiers=[],
      install_requires=[
            'requests >= 2.17.3',
            'colorama >= 0.3.7',
      ]
     )

