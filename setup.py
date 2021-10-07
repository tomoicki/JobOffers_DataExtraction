from setuptools import setup, find_packages

with open(file="README.md", mode="r") as readme_handle:
    long_description = readme_handle.read()

setup(
    name='job_offers_data_extraction',
    version='0.0.4',
    description='Job offers scraper for nofluffjobs.com and justjoin.it.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    python_requires=">=3.6",
    install_requires=[
        'joblib~=1.0',
        'pandas~=1.3',
        'requests~=2.26',
    ],
)
