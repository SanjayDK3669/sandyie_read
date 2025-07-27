<p align="center">
  <img src="https://sandyie.in/images/Logo.svg" width="140" alt="Sandyie Logo">
</p>

<h1 align="center">Sandyie Read 📚</h1>

<p align="center">
  <a href="https://pypi.org/project/sandyie-read/"><img src="https://img.shields.io/pypi/v/sandyie_read?color=blue" alt="PyPI version"></a>
  <a href="https://pypi.org/project/sandyie-read/"><img src="https://img.shields.io/pypi/dm/sandyie_read" alt="Downloads"></a>
  <a href="LICENSE"><img src="https://img.shields.io/github/license/sandyie/sandyie-read" alt="License"></a>
  <a href="https://www.python.org/downloads/"><img src="https://img.shields.io/badge/Python-3.7%2B-blue.svg" alt="Python Version"></a>
</p>

<p align="center"><strong>Effortlessly read files like PDFs, images, YAML, CSV, Excel, and more — powered by logging and custom exceptions.</strong></p>

---

## ⚠️ Python Compatibility

> 🐍 **This library requires Python 3.7+**.  
> ⚠️ Some features may not work properly in versions below Python 3.11. Please use **Python 3.11 or above** for best compatibility.

---

## 🔧 Features

- ✅ Read and extract content from:
  - PDF (text-based and scanned with OCR)
  - Image files (JPG, PNG)
  - YAML files
  - Text files
  - CSV, Excel
- 🧠 OCR support using Tesseract
- 📋 Human-readable logging
- 🛡️ Clean exception handling (`SandyieException`)

---

## 📦 Installation

```bash
pip install sandyie_read
```

---

## 🚀 Quick Start

```python
from sandyie_read import read

data = read("example.pdf")
print(data)
```

---

## 📁 Supported File Types & Examples

### 1. 📄 PDF (Text-based or Scanned)

```python
data = read("sample.pdf")
print(data)
```

🟢 **Returns:** A `string` containing extracted text. OCR is auto-applied to scanned files.

---

### 2. 🖼️ Image Files (PNG, JPG)

```python
data = read("photo.jpg")
print(data)
```

🟢 **Returns:** A `string` of OCR-extracted text.

---

### 3. ⚙️ YAML Files

```python
data = read("config.yaml")
print(data)
```

🟢 **Returns:** A `dictionary` representing the YAML structure.

---

### 4. 📄 Text Files (.txt)

```python
data = read("notes.txt")
print(data)
```

🟢 **Returns:** Plain text from file.

---

### 5. 📊 CSV Files

```python
data = read("data.csv")
print(data)
```

🟢 **Returns:** `pandas.DataFrame` with structured data.

---

### 6. 📈 Excel Files (.xlsx, .xls)

```python
data = read("report.xlsx")
print(data)
```

🟢 **Returns:** A `DataFrame` or dict of `DataFrames` for multi-sheet files.

---

## ⚠️ Error Handling

All exceptions are wrapped inside a custom `SandyieException`, making debugging simple and consistent.

---

## 🧪 Logging

Logs show:

- File type detection
- Success/failure for reads
- Detailed processing insights

---

## 📚 Auto-Generated Docs

Coming soon at 👉 **[https://sandyie.in/docs](https://sandyie.in/docs)**

It will include:

- 📘 API Reference
- ❌ Exception explanations
- 📓 Usage examples and notebooks

---

## 🤝 Contribute

Spotted a bug or have a new idea?  
Open an [Issue](https://github.com/sandyie/sandyie-read/issues) or send a Pull Request.

---

## 📄 License

Licensed under the **MIT License**.  
See [LICENSE](LICENSE) for more.

---

## 👤 Author

**Sanju (aka Sandyie)**  
🌐 Website: [www.sandyie.in](https://www.sandyie.in)  
📧 Email: [dksanjay39@gmail.com](mailto:dksanjay39@gmail.com)  
🐍 PyPI: [https://pypi.org/project/sandyie-read](https://pypi.org/project/sandyie-read)

---
