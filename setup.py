from setuptools import setup, find_packages
import avanza
import pypandoc

LONG_DESCRIPTION = pypandoc.convert_file('README.rst', 'md')

VERSION = avanza.__version__

setup(
    name="Avanza",
    version=VERSION,
    packages=find_packages(exclude=['contrib', 'docs', 'tests', 'examples']),
    install_requires=[
        "requests",
        "selenium",
        "pandas",
        ],
    package_data={},
    author="North14",
    description="Python wrapper for Unofficial Avanza API",
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    url="https://github.com/North14/avanza",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Topic :: Office/Business :: Financial",
        "Topic :: Office/Business :: Financial :: Investment",
        ],
    platforms=['any'],
    python_requires=">=3.6"
)
