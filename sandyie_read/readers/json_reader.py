import pandas as pd
import logging
from ..exceptions import SandyieException

logger = logging.getLogger(__name__)

def read_json(path):
    """
    Reads a JSON file and returns a pandas DataFrame.
    Assumes the JSON is either a list of records or a dict that can be normalized.
    """
    try:
        df = pd.read_json(path)
        logger.info(f"[JSONReader] Successfully read JSON file: {path}")
        return df
    except ValueError as e:
        raise SandyieException("The JSON file is malformed or unsupported", e)
    except Exception as e:
        raise SandyieException("Failed to read the JSON file", e)
