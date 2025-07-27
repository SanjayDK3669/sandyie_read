from setuptools import setup, find_packages
from pathlib import Path

# Read the long description from README.md
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text(encoding="utf-8")

setup(
    name="sandyie_read",
    version="0.4.9",                    
    author="Sanju (Sandyie)",
    author_email="dksanjay39@gmail.com",
    description="A lightweight Python library to read various data formats including PDF, images, YAML, and more.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/SanjayDK3669/sandyie_read",

    packages=find_packages(),
    include_package_data=True,

    # Support CPython 3.7 through 3.13
    python_requires=">=3.7, <3.14",

    install_requires=[
        "pandas>=2.1.0,<2.3",
        "numpy>=1.21.0",

        # on Python ≤3.10, use SciPy up through 1.10.x; on 3.11–3.13, up through 1.14.x
        "scipy>=1.7.0,<1.11; python_version < '3.11'",
        "scipy>=1.7.0,<1.15; python_version >= '3.11' and python_version < '3.14'",

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
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Text Processing :: General",
        "Topic :: Scientific/Engineering :: Information Analysis",
    ],
)
