from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="Avanza",
    version="0.0.7",
    packages=find_packages(exclude=['contrib', 'docs', 'tests', 'examples']),
    install_requires=[
        "requests",
        "selenium",
        ],
    package_data={},
    author="North14",
    description="Python wrapper for Unofficial Avanza API",
    long_description=long_description,
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
