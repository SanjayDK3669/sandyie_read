import pickle
import logging
from sandyie_read.exceptions import SandyieException

logger = logging.getLogger(__name__)

def read_pickle(path):
    """
    Reads a .pickle or .pkl file and returns the deserialized Python object.
    """
    try:
        with open(path, "rb") as f:
            obj = pickle.load(f)
        logger.info("[PickleReader] Successfully read Pickle file: {}".format(path))
        return obj
    except Exception as e:
        raise SandyieException("Failed to read the .pickle/.pkl file", e)
