import logging
from sandyie_read.exceptions import SandyieException

logger = logging.getLogger(__name__)

def read_js(path):
    """
    Reads a .js (JavaScript) file and returns its content as plain text.
    This is useful for viewing or analyzing raw JS code.
    """
    try:
        with open(path, "r", encoding="utf-8") as f:
            content = f.read()
            logger.info(f"[JSReader] Successfully read JS file: {path}")
            return content
    except FileNotFoundError as e:
        raise SandyieException("JavaScript file not found", e)
    except UnicodeDecodeError as e:
        raise SandyieException("Could not decode the JavaScript file", e)
    except Exception as e:
        raise SandyieException("Failed to read the JavaScript file", e)
