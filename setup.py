from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()

# Get the long description from the README file
long_description = (here / "README.rst").read_text(encoding="utf-8")

with open("autoanno/__init__.py") as file:
    for line in file:
        if line.startswith("__version__"):
            version = line.strip().split()[-1][1:-1]
            break


def parse_requirements_file(filename):
    with open(filename) as file:
        requires = [l.strip() for l in file.readlines() if not l.startswith("#")]
    return requires


install_requires = parse_requirements_file("requirements/default.txt")
extras_require = {
    dep: parse_requirements_file("requirements/" + dep + ".txt")
    for dep in ["docs", "test"]
}

setup(
    # There are some restrictions on what makes a valid project name
    # specification here:
    # https://packaging.python.org/specifications/core-metadata/#name
    name="autoanno",  # Required
    # For a discussion on single-sourcing the version across setup.py and the
    # project code, see
    # https://packaging.python.org/en/latest/single_source_version.html
    version=version,  # Required
    description="Investigation into using AutoML and Topological Data Analysis for Automated Annotation",
    long_description=long_description,
    long_description_content_type="text/x-rst",
    url="https://autoanno.readthedocs.io/en/latest/index.html",  # Optional
    author="Matthew Gudorf",
    author_email="matthew.gudorf@gmail.com",  # Optional
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Information Technology",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: Microsoft :: Windows :: Windows 10",
    ],
    packages=find_packages(include=["autoanno", "autoanno.*"]),
    python_requires=">=3.7",
    install_requires=install_requires,
    extras_require=extras_require,
    project_urls={
                "documentation": "https://autoanno.readthedocs.io/en/latest/index.html",
                "source": "https://github.com/mgudorf/autoanno",
                "tutorials": "https://github.com/mgudorf/autoanno/tree/main/notebooks",
    },
    package_data={"autoanno": ["requirements/*.txt"]}
)
