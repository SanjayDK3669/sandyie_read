import io
import logging
from sandyie_read.exceptions import SandyieException

logger = logging.getLogger(__name__)

def read_svg(path):
    """
    Reads an .svg file and returns its raw XML (as a string).
    """
    try:
        with io.open(path, mode="r", encoding="utf-8", errors="ignore") as f:
            content = f.read()
        logger.info("[SVGReader] Successfully read SVG file: {}".format(path))
        return content
    except Exception as e:
        raise SandyieException("Failed to read the .svg file", e)
