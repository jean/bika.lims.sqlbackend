# -*- coding: utf-8 -*-
"""Installer for the bika.lims.sqlbackend package."""

from setuptools import find_packages
from setuptools import setup


long_description = (
    open('README.rst').read()
    + '\n' +
    'Contributors\n'
    '============\n'
    + '\n' +
    open('CONTRIBUTORS.rst').read()
    + '\n' +
    open('CHANGES.rst').read()
    + '\n')


setup(
    name='bika.lims.sqlbackend',
    version='0.1',
    description="Mirror facets of Bika data to SQL for analysis and integration",
    long_description=long_description,
    # Get more from http://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        "Environment :: Web Environment",
        "Framework :: Plone",
        "Framework :: Plone :: 4.3.6",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
    ],
    keywords='Python Plone',
    author='Jean Jordaan',
    author_email='jean.jordaan@gmail.com',
    url='http://pypi.python.org/pypi/bika.lims.sqlbackend',
    license='GPL',
    packages=find_packages('src', exclude=['ez_setup']),
    namespace_packages=['bika', 'bika.lims'],
    package_dir={'': 'src'},
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'plone.api',
        'setuptools',
        'z3c.jbot',
        'bika.lims',
        'transmogrifier',
        'z3c.autoinclude',
        'venusianconfiguration',
    ],
    extras_require={
        'test': [
            'plone.app.testing',
            'plone.app.contenttypes',
            'plone.app.robotframework[debug]',
        ],
    },
    entry_points="""
    [z3c.autoinclude.plugin]
    target = plone
    """,
)
