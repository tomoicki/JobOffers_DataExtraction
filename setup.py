import setuptools


setuptools.setup(
    name='JobOffers_DataExtraction',
    version='0.0.1',
    author="TJ",
    description="A small example package",
    url='https://github.com/tomoicki/JobOffers_DataExtraction/tree/using_requests',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "utilities"},
    packages=setuptools.find_packages(where="utilities"),
    python_requires=">=3.6",
)