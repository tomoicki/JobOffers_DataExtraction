from setuptools import setup

with open(file="README.md", mode="r") as readme_handle:
    long_description = readme_handle.read()

setup(
    name='JobOffers_DataExtraction',
    version='0.0.1',
    description='Job offers scraper for nofluffjobs.com and justjoin.it.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/tomoicki/JobOffers_DataExtraction/tree/using_requests',
    packages=["utilities"],
    install_requires=[
        'requests == 2.26.0',
        'pandas == 1.3.2',
        'joblib == 1.0.1',
    ],
)
