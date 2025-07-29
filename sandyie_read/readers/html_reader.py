import io
import logging
from bs4 import BeautifulSoup
from sandyie_read.exceptions import SandyieException

logger = logging.getLogger(__name__)

def read_html(path):
    """
    Reads an .html or .htm file and returns its text content as a single string,
    with blocks separated by newline characters.

    Compatible with Python 2.7 and all Python 3.x versions.
    """
    try:
        # open in universal text mode
        with io.open(path, 'r', encoding='utf-8', errors='ignore') as f:
            html = f.read()

        soup = BeautifulSoup(html, 'html.parser')
        # extract visible text, separating blocks by newline
        blocks = []
        for elem in soup.stripped_strings:
            blocks.append(elem)
        text = "\n".join(blocks)

        logger.info("[HTMLReader] Successfully read HTML file: {}".format(path))
        return text
    except Exception as e:
        raise SandyieException("Failed to read the HTML/HTM file", e)
