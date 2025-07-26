import pandas as pd
import logging
from ..exceptions import SandyieException

logger = logging.getLogger(__name__)

def read_excel(path):
    """
    Reads an Excel file (.xls or .xlsx) and returns a pandas DataFrame.
    """
    try:
        df = pd.read_excel(path)
        logger.info(f"[ExcelReader] Successfully read Excel file: {path}")
        return df
    except Exception as e:
        raise SandyieException("Failed to read the Excel file", e)
