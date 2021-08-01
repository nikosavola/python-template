import os
from setuptools import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name="PythonTemplate",
    version=0.1,
    description="Python template",
    long_description=read('README.md'),
    author="Niko Savola",
    author_email="niko.savola@aalto.fi",
    license="MIT",
    url="https://github.com/nikosavola/python-template",
    packages=['project_name'],
    python_requires=">=3.6.9,<3.10",
    install_requires=[
        "numpy>=1.16",
    ],
    extras_require={
        "docs": [
            "sphinx~=4.1",
            "sphinx-rtd-theme~=0.5"
        ],
        "test": [
            "pytest>=6.1",
            "pytest-sugar>=0.9",
            "pytest-cov>=2.12",
            "pytest-xdist>=2.3",
            "pylint>=2.9"
        ],
    },
)
