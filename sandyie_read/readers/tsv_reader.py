import pandas as pd
import logging
from sandyie_read.exceptions import SandyieException

logger = logging.getLogger(__name__)

def read_tsv(path):
    """
    Reads a TSV (.tsv) file and returns a pandas DataFrame.
    """
    try:
        df = pd.read_csv(path, sep="\t")
        logger.info("[TSVReader] Successfully read TSV file: {}".format(path))
        return df
    except Exception as e:
        raise SandyieException("Failed to read the TSV file", e)
