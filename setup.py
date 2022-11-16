from distutils.core import setup

import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="src",

    version="0.0.1",

    author="notanna",

    packages=setuptools.find_packages(include=['src', 'src.*']),

    include_package_data=True,

    url="https://github.com/n0tanna/mupy",

    description="A constantly in-progress math package.",

    long_description=long_description,
    long_description_content_type="text/markdown",

    install_requires=[
        'attrs==22.1.0',
        'iniconfig==1.1.1',
        'packaging==21.3',
        'pluggy==1.0.0',
        'py==1.11.0',
        'pyparsing==3.0.9',
        'tomli==2.0.1',
    ],
)
