"""A Python library to download meteorological data of campaign GoAmazon.

Author Adriano P. ALmeida <adriano.almeida@inpe.br>
License: MIT

See:
https://github.com/AdrianoAlmeida/goamazondownloader
"""

from setuptools import setup, find_packages
import pathlib
import sys
import os

HERE = pathlib.Path(__file__).parent.resolve()
LONG_DESCRIPTION = (HERE / 'README.md').read_text(encoding='utf-8')

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist bdist_wheel')
    os.system('twine upload dist/*')
    sys.exit()

if sys.argv[-1] == 'uninstall':
    os.system('rm -rf build')
    os.system('rm -rf dist')
    os.system('rm -rf goamazondownloader.egg-info')
    sys.exit()


setup(
    name='goamazondownloader',
    version='0.1.3',
    description='A library python to download data of campaign GoAmazon',
    long_description=LONG_DESCRIPTION,
    long_description_content_type='text/markdown',
    url='https://github.com/AdrianoPereira/goamazondownloader',
    author='Adriano P. Almeida',
    author_email='adriano.almeida@inpe.br',
    classifiers = [
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',


        # Specify the Python versions you support here. In particular, ensure
        # that you indicate you support Python 3. These classifiers are *not*
        # checked by 'pip install'. See instead 'python_requires' below.
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3 :: Only',
    ],
    keywords = 'data weather, goamazon, sipam, starnet',
    packages = find_packages(where=HERE),  # Required
    python_requires = '>=3.5, <4',
    install_requires = ['requests', 'beautifulsoup4'],
    project_urls = {
        'Bug Reports': 'https://github.com/AdrianoPereira/goamazondownloader/issues',
        'Say Thanks!': 'http://adrianopereira.github.io',
        'Source': 'https://github.com/AdrianoPereira/goamazondownloader',
    },
    license = 'MIT'
)