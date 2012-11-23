# Importing setuptools is optional, but adds some features
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name = "Genutiv",
    version = "0.1",
    description = "Test accuracy of patterns to predict gender of German nouns.",
    long_description  = open("README.md").read(),
    url = "http://pamolloy.dyndns.org/project/genutiv/",
    download_url = "http://github.com/pamolloy/Genutiv",
    author = "Philip Molloy",
    author_email = "philip.a.molloy+genutiv@gmail.com",
    license = "",   #TODO Select a GPL-compatible license
    classifiers = [],   #TODO Select classifiers from list on PyPI
    install_requires = ["re","json","urllib2","wikitools"],
    packages = ["genutiv"],
)

