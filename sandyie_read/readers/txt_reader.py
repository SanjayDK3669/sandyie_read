import os
from sandyie_read.exceptions import SandyieException
import logging

logger = logging.getLogger(__name__)

def read_txt(file_path: str) -> str:
    try:
        if not os.path.exists(file_path):
            raise SandyieException(f"Text file not found: {file_path}")

        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()

        logger.info(f"Successfully read TXT file: {file_path}")
        return content

    except Exception as e:
        raise SandyieException(f"Failed to read TXT file: {file_path}. Error: {str(e)}")
