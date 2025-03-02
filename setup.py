import setuptools
from distutils.core import setup
#python setup.py bdist_wheel --universal

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="NorenRestApiPy",
    version="0.0.22",
    author="KumarAnand",
    author_email="kumar.anand@kambala.co.in",
    description="A package for NorenOMS",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: Other/Proprietary License",
        "Operating System :: OS Independent",
    ),
    install_requires=[
    ],
)



