# setup.py

from setuptools import setup, find_packages

setup(
    name="textutils",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        'nltk',
    ],
    author="Alphonse",
    author_email="solofondraibedani@gmail.com",
    description="Une bibliothèque pour la manipulation de texte",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/Alphonse-code/textutils",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
