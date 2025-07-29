import logging
from sandyie_read.exceptions import SandyieException

# Import all readers
from sandyie_read.readers.csv_reader import read_csv
from sandyie_read.readers.excel_reader import read_excel
from sandyie_read.readers.json_reader import read_json
from sandyie_read.readers.js_reader import read_js
from sandyie_read.readers.txt_reader import read_txt
from sandyie_read.readers.pdf_reader import read_pdf
from sandyie_read.readers.image_reader import read_image
from sandyie_read.readers.ocr_reader import read_ocr
from sandyie_read.readers.yaml_reader import read_yaml
from sandyie_read.readers.html_reader import read_html
from sandyie_read.readers.docx_reader import read_docx
from sandyie_read.readers.markdown_reader import read_md
from sandyie_read.readers.tsv_reader import read_tsv
from sandyie_read.readers.bin_reader import read_bin
from sandyie_read.readers.pickle_reader import read_pickle
from sandyie_read.readers.parquet_reader import read_parquet
from sandyie_read.readers.svg_reader import read_svg
from sandyie_read.readers.zip_reader import read_zip


logger = logging.getLogger(__name__)


def read(file_path):
    """
    Main function to read various file types.
    """
    try:
        ext = file_path.split('.')[-1].lower()

        if ext == "csv":
            return read_csv(file_path)
        elif ext == "tsv":
            return read_tsv(file_path)
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
        elif ext in ["html", "htm"]:
            return read_html(file_path)
        elif ext in ["docx"]:
            return read_docx(file_path)
        elif ext in ["md", "markdown"]:
            return read_md(file_path)
        elif ext in ["bin"]:
            return read_bin(file_path)
        elif ext in ["pickle", "pkl"]:
            return read_pickle(file_path)
        elif ext in ["parquet"]:
            return read_parquet(file_path)
        elif ext in ["svg"]:
            return read_svg(file_path)
        elif ext in ["zip"]:
            return read_zip(file_path)
        else:
            raise SandyieException(f"Unsupported file extension: .{ext}")
    
    except SandyieException as e:
        logger.error(str(e))
        raise
    except Exception as e:
        logger.exception("Unexpected error occurred while reading the file.")
        raise SandyieException(f"Unexpected error: {e}")
