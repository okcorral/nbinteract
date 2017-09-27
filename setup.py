"""
A Jupyter subcommand to export notebooks and their widgets to publicly
runnable HTML files.
"""

# Always prefer setuptools over distutils
from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='nbinteract',
    version='0.0.1.dev1',
    description='Jupyter subcommand to export interactive HTML pages',
    long_description=long_description,
    url='https://github.com/SamLau95/nbinteract',

    author='Sam Lau',
    author_email='samlau95@gmail.com',

    license='MIT',

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Development Status :: 3 - Alpha',

        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',

        'License :: OSI Approved :: MIT License',

        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Framework :: Jupyter',
    ],
    keywords='jupyter nbconvert interact',

    packages=find_packages(exclude=['contrib', 'docs', 'tests']),
    install_requires=['nbconvert'],

    extras_require={
        'dev': ['check-manifest'],
        'test': ['coverage'],
    },

    # To provide executable scripts, use entry points in preference to the
    # "scripts" keyword. Entry points provide cross-platform support and allow
    # pip to create the appropriate form of executable for the target platform.
    entry_points={
        'console_scripts': [
            'jupyter-nbinteract = nbinteract.nbinteractapp:main',
        ],
    },
)