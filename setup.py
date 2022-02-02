#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [ ]

test_requirements = [ ]

setup(
    author="Marina Ruiz Sanchez-Oro[D[D[D[D[D[D[D[D[D[Dá",
    author_email='marina.ruiz.so@ed.ac.uk',
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="test for creating a cppackage",
    entry_points={
        'console_scripts': [
            'pypackage_test=pypackage_test.cli:main',
        ],
    },
    install_requires=requirements,
    license="MIT license",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='pypackage_test',
    name='pypackage_test',
    packages=find_packages(include=['pypackage_test', 'pypackage_test.*']),
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/MarinaRuizSO/pypackage_test',
    version='[0.1.0]',
    zip_safe=False,
)
