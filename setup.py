from setuptools import setup, find_packages
from os import path
from io import open

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
     long_description = f.read()

setup(
    name="digibit",
    version="1.0",
    author="Deepak Gupta",
    author_email="gdeepak884@gmail.com",
    description="Python Digital value problem solver",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/gdeepak884/bits",
    packages=find_packages(),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
      python_requires='>=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*, <4',
      project_urls={ 
        'Bug Reports': 'https://github.com/gdeepak884/digibit/issues',
        'Source': 'https://github.com/gdeepak884/digibit',
},
)
