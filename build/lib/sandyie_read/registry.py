from sandyie_read.readers.csv_reader import read_csv
from sandyie_read.readers.excel_reader import read_excel
from sandyie_read.readers.json_reader import read_json
from sandyie_read.readers.js_reader import read_js
from sandyie_read.readers.pdf_reader import read_pdf
from sandyie_read.readers.image_reader import read_image
from sandyie_read.readers.txt_reader import read_txt

# Registry to map file extensions to reader functions
READER_REGISTRY = {
    '.csv': read_csv,
    '.xlsx': read_excel,
    '.xls': read_excel,
    '.json': read_json,
    '.js': read_js,
    '.pdf': read_pdf,
    '.png': read_image,
    '.jpg': read_image,
    '.jpeg': read_image,
    '.txt': read_txt,
}
