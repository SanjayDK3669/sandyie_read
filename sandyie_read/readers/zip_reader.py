import zipfile
import pandas as pd
import logging
from io import BytesIO
from sandyie_read.exceptions import SandyieException

logger = logging.getLogger(__name__)

def read_zip(path):
    """
    Reads a .zip file containing one supported file (.csv, .tsv, .xls, .xlsx)
    and returns its content as a pandas DataFrame.
    """
    try:
        with zipfile.ZipFile(path, 'r') as z:
            # Filter for supported file types
            supported_exts = ('.csv', '.tsv', '.xls', '.xlsx')
            supported_files = [f for f in z.namelist() if f.lower().endswith(supported_exts)]

            if not supported_files:
                raise SandyieException("No supported files (.csv, .tsv, .xls, .xlsx) found in the ZIP archive.", None)

            # Read the first supported file
            file_name = supported_files[0]
            with z.open(file_name) as f:
                if file_name.endswith('.csv'):
                    df = pd.read_csv(f)
                elif file_name.endswith('.tsv'):
                    df = pd.read_csv(f, sep='\t')
                else:
                    df = pd.read_excel(f)

            logger.info("[ZipReader] Successfully read '{}' from ZIP: {}".format(file_name, path))
            return df

    except Exception as e:
        raise SandyieException("Failed to read the .zip file", e)
