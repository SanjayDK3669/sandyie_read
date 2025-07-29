import pandas as pd
import logging
from sandyie_read.exceptions import SandyieException

logger = logging.getLogger(__name__)

def read_parquet(path):
    """
    Reads a .parquet file and returns a pandas DataFrame.
    Requires 'pyarrow' or 'fastparquet' engine.
    """
    try:
        df = pd.read_parquet(path)  # pandas will auto-detect engine
        logger.info("[ParquetReader] Successfully read Parquet file: {}".format(path))
        return df
    except Exception as e:
        raise SandyieException("Failed to read the .parquet file", e)
