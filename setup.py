from setuptools import setup, find_packages
setup(
    name="Avanza",
    version="0.1",
    packages=find_packages(exclude=["tests", "*.tests", "*.tests.*", "tests.*"]),
    install_requires=["requests"],
    package_data={
    },

    author="Me",
    author_email="me@example.com",
    description="This is an Example Package",
    keywords="hello world example examples",
    url="http://example.com/HelloWorld/",
    classifiers=[
        "License :: OSI Approved :: MTI License"
    ]
)
