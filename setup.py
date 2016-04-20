import os
from setuptools import setup, find_packages

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "PythonCommon",
    version = "1.0.0",

    author = "Andrew Ongko",
    author_email = "Andrew.Ongko@gmail.com",

    url = "https://github.com/aongko/PythonCommon",
    description = "some basic functionality for python apps",
    long_description = read("README.md"),
    keywords = "python",

    license = "MIT License",

    packages=find_packages('src', exclude=['contrib', 'docs', 'tests']),
    package_dir = {'': 'src'},

    classifiers = [
        "Development Status :: 3 - Alpha",
        # "Development Status :: 4 - Beta",
        # "Development Status :: 5 - Production/Stable",
        # "Development Status :: 6 - Mature",
        # "Development Status :: 7 - Inactive",

        "Intended Audience :: Developers",

        "License :: OSI Approved :: MIT License",

        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
    ],
    install_requires = [
        "langdetect==1.0.5",
        "pymongo==3.2.2",
        "PyMySQL==0.7.2",
        "requests==2.9.1"
    ]
)
