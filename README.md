# Sandyie Read 📚

A Python library to read and extract data from various file formats including PDF, images, YAML, and more.

## Features
- Read from PDFs, PNGs, JPGs, YAML, etc.
- OCR support for scanned files
- Clean logging and exception handling

## Installation
```bash
pip install sandyie_read


example 
from sandyie_read import read

data = read("example.pdf")
print(data)
