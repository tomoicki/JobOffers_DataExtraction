from setuptools import setup
from setuptools import find_packages

# Load the README file.
with open(file="README.md", mode="r") as readme_handle:
    long_description = readme_handle.read()

setup(
    name='JobOffers_DataExtraction',
    version='0.0.1',
    description='A python client library used to leverage the different libraries provided by Sigma Coding.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/tomoicki/JobOffers_DataExtraction/tree/using_requests',
    packages=find_packages(exclude=["tests"]),
    install_requires=[
        'requests == 2.26.0',
        'pandas == 1.3.2',
        'joblib == 1.0.1',
    ],
)
