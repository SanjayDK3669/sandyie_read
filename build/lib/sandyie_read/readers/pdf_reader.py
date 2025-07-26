import fitz  # PyMuPDF
from ..exceptions import SandyieException
import logging

logger = logging.getLogger(__name__)

def read_pdf(file_path: str) -> str:
    """
    Reads the text content from a PDF file.

    Args:
        file_path (str): Path to the PDF file.

    Returns:
        str: Extracted text from the PDF.

    Raises:
        SandyieException: If the PDF cannot be read.
    """
    try:
        logger.info(f"Reading PDF file: {file_path}")
        with fitz.open(file_path) as doc:
            text = ""
            for page in doc:
                text += page.get_text()
        return text.strip()
    except FileNotFoundError:
        logger.error(f"PDF file not found: {file_path}")
        raise SandyieException(f"PDF file not found: {file_path}")
    except Exception as e:
        logger.exception("Failed to read PDF file.")
        raise SandyieException(f"Failed to read PDF file: {str(e)}")
