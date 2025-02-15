from setuptools import setup, find_packages

setup(
    name="pytranslateinglish",
    version="0.1.2",
    packages=find_packages(),
    install_requires=[
        "torch",
        "transformers",
        "pymupdf",
    ],
    author="FredyVaron",
    author_email="fvaron2511@gmail.com",
    description="Librería para traducir texto y PDFs entre inglés - español O Español - Ingles",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/fredyvaron/pytranslateinglish",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)