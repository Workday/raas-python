from setuptools import setup
import versioneer

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="raas",
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
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
