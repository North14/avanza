from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="Avanza",
    version="0.0.4",
    packages=find_packages(exclude=["tests", "*.tests", "*.tests.*", "tests.*"]),
    install_requires=["requests"],
    package_data={},
    author="North14",
    description="Python wrapper for Unofficial Avanza API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/North14/avanza",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License"
    ],
    python_requires=">=3.7"
)
