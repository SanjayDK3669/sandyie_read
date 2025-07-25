import os

PROJECT_NAME = "sandyie_read"

files = [
    "pyproject.toml",
    "README.md",
    "LICENSE",
    f"{PROJECT_NAME}/__init__.py",
    f"{PROJECT_NAME}/core.py",
    f"{PROJECT_NAME}/exceptions.py",
    f"{PROJECT_NAME}/logging_config.py",
    f"{PROJECT_NAME}/utils.py",
    f"{PROJECT_NAME}/registry.py",
    f"{PROJECT_NAME}/readers/__init__.py",
    f"{PROJECT_NAME}/readers/base.py",
    f"{PROJECT_NAME}/readers/csv_reader.py",
    f"{PROJECT_NAME}/readers/excel_reader.py",
    f"{PROJECT_NAME}/readers/json_reader.py",
    f"{PROJECT_NAME}/readers/js_reader.py",
    f"{PROJECT_NAME}/readers/txt_reader.py",
    f"{PROJECT_NAME}/readers/pdf_reader.py",
    f"{PROJECT_NAME}/readers/image_reader.py",
    f"{PROJECT_NAME}/readers/ocr_reader.py",
    f"{PROJECT_NAME}/readers/yaml_reader.py",
    "tests/__init__.py",
    "tests/test_core.py",
    "tests/test_readers_csv.py",
    "tests/test_readers_excel.py",
    "tests/test_readers_txt_pdf.py",
    "tests/test_readers_yaml.py"
]

def create_file_structure():
    for file in files:
        path = os.path.join(os.getcwd(), file)
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "w", encoding="utf-8") as f:
            f.write("")  # empty content

    print("✅ File structure created.")

if __name__ == "__main__":
    create_file_structure()
