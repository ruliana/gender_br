import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="gender_guess",
    version="0.0.1",
    author="Ronie Uliana",
    author_email="ronie.uliana@gmail.com",
    description="Gender guessing for Portuguese first names",
    long_description="Gender guessing for Portuguese first names",
    long_description_content_type="text/markdown",
    url="https://github.com/ruliana/gender_guess",
    packages=setuptools.find_packages(),
    install_requires=[
        "unidecode"
    ],
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)
