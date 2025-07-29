import logging
from sandyie_read.exceptions import SandyieException

logger = logging.getLogger(__name__)

def read_bin(path):
    """
    Reads a .bin file and returns its raw content as bytes.
    """
    try:
        with open(path, "rb") as f:
            content = f.read()
        logger.info("[BinReader] Successfully read BIN file: {}".format(path))
        return content
    except Exception as e:
        raise SandyieException("Failed to read the .bin file", e)
