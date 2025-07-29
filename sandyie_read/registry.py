from sandyie_read.readers.csv_reader import read_csv
from sandyie_read.readers.excel_reader import read_excel
from sandyie_read.readers.json_reader import read_json
from sandyie_read.readers.js_reader import read_js
from sandyie_read.readers.pdf_reader import read_pdf
from sandyie_read.readers.image_reader import read_image
from sandyie_read.readers.txt_reader import read_txt
from sandyie_read.readers.yaml_reader import read_yaml
from sandyie_read.readers.html_reader import read_html
from sandyie_read.readers.ocr_reader import read_ocr
from sandyie_read.readers.docx_reader import read_docx
from sandyie_read.readers.markdown_reader import read_md
from sandyie_read.readers.tsv_reader import read_tsv
from sandyie_read.readers.bin_reader import read_bin
from sandyie_read.readers.pickle_reader import read_pickle
from sandyie_read.readers.parquet_reader import read_parquet
from sandyie_read.readers.svg_reader import read_svg
from sandyie_read.readers.zip_reader import read_zip



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
    '.yaml' : read_yaml,
    '.yml': read_yaml,
    '.html': read_html,
    '.htm': read_html,
    '.ocr': read_ocr, 
    '.docx': read_docx,
    '.m': read_md,
    '.tsv': read_tsv,
    '.bin':read_bin,
    'pickle':read_pickle,
    'pkl':read_pickle,
    '.parquet': read_parquet,
    'svg': read_svg,
    'zip':read_zip
}
