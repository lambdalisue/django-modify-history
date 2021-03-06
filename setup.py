#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author:       Alisue
# Last Change:  18-Mar-2011.
#
from setuptools import setup, find_packages

version = "0.1rc1"

def read(filename):
    import os.path
    return open(os.path.join(os.path.dirname(__file__), filename)).read()
setup(
        name="django-modify-history",
        version=version,
        description = "Automatically create history database when perticular model is saved.",
        long_description=read('README.mkd'),
        classifiers = [
            'Framework :: Django',
            'Intended Audience :: Developers',
            'License :: OSI Approved :: BSD License',
            'Programming Language :: Python',
            'Topic :: Internet :: WWW/HTTP',
        ],
        keywords = "django history modify",
        author = "Alisue",
        author_email = "alisue@hashnote.net",
        url=r"https://github.com/alisue/django-modify-history",
        download_url = r"https://github.com/alisue/django-modify-history/tarball/master",
        license = 'BSD',
        packages = find_packages(),
        include_package_data = False,
        zip_safe = True,
        install_requires=['setuptools'],
)
