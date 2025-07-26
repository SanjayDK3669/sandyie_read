import pandas as pd
import logging
from sandyie_read.exceptions import SandyieException

logger = logging.getLogger(__name__)

def read_csv(path):
    """
    Reads a CSV file and returns a pandas DataFrame.
    """
    try:
        df = pd.read_csv(path)
        logger.info(f"[CSVReader] Successfully read CSV file: {path}")
        return df
    except Exception as e:
        raise SandyieException("Failed to read the CSV file", e)
