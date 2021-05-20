#!/usr/bin/env python3

import sys, requests
from setuptools import setup, find_packages

setup(
    name='cluwards',
    version='1.1.1',
    author='Max Bridgland',
    author_email='mabridgland@protonmail.com',
    description='CLUCoin Reward Tracker',
    long_description=open('README.md', 'r').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/M4cs/Cluwards',
    packages=find_packages(include=['cluwards']),
    install_requires=[
        'rich',
        'web3'
    ],
    project_urls={
        'Wiki': 'https://github.com/M4cs/cluwards'
    },
    license='GNU General Public License v3 (GPLv3) (GPL)',
    zip_safe=True,
    entry_points={
        'console_scripts':[
            'cluwards = cluwards.__main__:main',
        ],
    },
    tests_require=[
        'mock;python_version<"3"',
        'pytest',
        'pytest-cov'
    ],
    classifiers=[  # Used by PyPI to classify the project and make it searchable
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',

        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',

        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Programming Language :: Python :: Implementation :: IronPython',
        'Programming Language :: Python :: Implementation :: Jython',

        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Intended Audience :: Information Technology',

        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Software Development :: Libraries',
        'Topic :: System :: Systems Administration',
        'Topic :: System :: Networking',
        'Topic :: Utilities',
    ]
)
