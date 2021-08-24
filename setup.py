from setuptools import setup

setup(
    name='JobOffers_DataExtraction',
    version='0.0.1',
    packages=['utilities'],
    install_requires=[
        'requests == 2.26.0',
        'pandas == 1.3.2',
        'joblib == 1.0.1',
    ],
)
