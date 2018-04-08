import os
import re
from setuptools import setup, find_packages


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name = 'pyxhook',
    version = '0.1.0',
    author = 'Kris',
    author_email = '31852063+krisfris@users.noreply.github.com',
    description = (''),
    license = read('license.txt'),
    keywords = '',
    url = '',
    packages=find_packages(),
    long_description=read('README.md'),
    classifiers=[],
    data_files = [('', ['license.txt', 'README.md'])],
    install_requires = []
)
