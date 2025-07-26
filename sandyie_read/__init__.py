import logging
from sandyie_read.exceptions import SandyieException

# Import all readers
from readers.csv_reader import read_csv
from readers.excel_reader import read_excel
from readers.json_reader import read_json
from readers.js_reader import read_js
from readers.txt_reader import read_txt
from readers.pdf_reader import read_pdf
from readers.image_reader import read_image
from readers.ocr_reader import read_ocr
from readers.yaml_reader import read_yaml

logger = logging.getLogger(__name__)


def read(file_path):
    """
    Main function to read various file types.
    """
    try:
        ext = file_path.split('.')[-1].lower()

        if ext == "csv":
            return read_csv(file_path)
        elif ext in ["xls", "xlsx"]:
            return read_excel(file_path)
        elif ext == "json":
            return read_json(file_path)
        elif ext == "js":
            return read_js(file_path)
        elif ext in ["txt", "log"]:
            return read_txt(file_path)
        elif ext == "pdf":
            return read_pdf(file_path)
        elif ext in ["jpg", "jpeg", "png"]:
            return read_image(file_path)
        elif ext == "ocr":  
            return read_ocr(file_path)
        elif ext in ["yaml", "yml"]:
            return read_yaml(file_path)
        else:
            raise SandyieException(f"Unsupported file extension: .{ext}")
    
    except SandyieException as e:
        logger.error(str(e))
        raise
    except Exception as e:
        logger.exception("Unexpected error occurred while reading the file.")
        raise SandyieException(f"Unexpected error: {e}")
