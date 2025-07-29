import docx
import logging
from sandyie_read.exceptions import SandyieException

logger = logging.getLogger(__name__)

def read_docx(path):
    """
    Reads a .docx file and returns its full text as a single string,
    with paragraphs separated by newline characters.

    Compatible with Python 2.7 and all Python 3.x versions.
    """
    try:
        doc = docx.Document(path)
        # Collect text from each paragraph
        paragraphs = []
        for para in doc.paragraphs:
            paragraphs.append(para.text)
        full_text = "\n".join(paragraphs)
        logger.info("[DocxReader] Successfully read DOCX file: {}".format(path))
        return full_text
    except Exception as e:
        # Wrap any error in your custom exception
        raise SandyieException("Failed to read the DOCX file", e)
