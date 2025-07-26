from setuptools import setup, find_packages
from pathlib import Path

# --- Read the README for long description ---
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text(encoding="utf-8")


# --- Project Metadata ---
PROJECT_NAME = "sandyie_read"
VERSION = "0.4.2"  
AUTHOR = "Sanju (Sandyie)"
AUTHOR_EMAIL = "dksanjay39@gmail.com"
DESCRIPTION = "A lightweight Python library to read various data formats including PDF, images, YAML, and more."
REPO_URL = "https://github.com/SanjayDK3669/sandyie_read"

setup(
    name=PROJECT_NAME,
    version=VERSION,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=REPO_URL,

    packages=find_packages(),

    install_requires=[
        "pandas>=1.3.0,<2.1",
        "numpy>=1.21.6,<1.25",
        "scipy>=1.7.0,<1.11",
        "opencv-python",
        "PyMuPDF",
        "pytesseract",
        "PyYAML",
        "Pillow",
        "pdfplumber",
        "openpyxl",
    ],

    license="MIT",

    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Text Processing :: General",
        "Topic :: Scientific/Engineering :: Information Analysis",
    ],

    python_requires=">=3.7",
)
