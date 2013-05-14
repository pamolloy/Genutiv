# Importing setuptools is optional, but adds some features
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name = 'Genutiv',
    version = '0.1.0',
    description = 'Test accuracy of patterns to predict gender of German nouns.',
    long_description  = open('README.md').read(),
    url = 'http://philipmolloy.com/project/genutiv/',
    download_url = 'http://github.com/pamolloy/Genutiv',
    author = 'Philip Molloy',
    author_email = 'philip.a.molloy+genutiv@gmail.com',
    license = '',   # TODO(PM) Select a GPL-compatible license
    classifiers = [],   # TODO(PM) Select classifiers from list on PyPI
    requires = ['re','json','urllib2','wikitools'],
    packages = ['genutiv', 'genutiv.analysis', 'genutiv.reference'],
    #package_data = []	# TODO(PM) Add package data
    #data_files = []	# TODO(PM) Add data files
)
