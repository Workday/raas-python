from setuptools import setup

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="raas",
    version="0.1.0",
    description="Python API client to download data from Report-as-a-Service (RaaS)",
    author="Curtis Hampton",
    author_email="CurtLHampton@gmail.com",
    url="https://github.com/Workday/raas-python",
    packages=["raas"],
    package_data={"raas": ["data/*"]},
    entry_points={"console_scripts": ["raas=raas.cli:main"]},
    install_requires=requirements,
    extras_require={"dev": ["pytest"]},
    keywords="raas",
    classifiers=["Programming Language :: Python :: 3.6", "Programming Language :: Python :: 3.7"],
)
