import setuptools
from setuptools import find_namespace_packages

# Load the README file.
with open(file="README.md", mode="r") as readme_handle:
    long_description = readme_handle.read()

setuptools.setup(
    name='JobOffers_DataExtraction',
    version='0.0.1',
    author="TJ",
    description="A small example package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/tomoicki/JobOffers_DataExtraction/tree/using_requests',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "JobOffers_DataExtraction"},
    packages=find_namespace_packages(where="utilities"),
    python_requires=">=3.6",
)
