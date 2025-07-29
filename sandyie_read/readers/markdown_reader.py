# markdown_reader.py

import io
import logging
from sandyie_read.exceptions import SandyieException

logger = logging.getLogger(__name__)

def read_md(path):
    """
    Reads a Markdown file with extension `.md` and returns its content as a string.

    :param path: Path to the `.md` file
    :return: str – the raw Markdown text
    """
    try:
        with io.open(path, 'r', encoding='utf-8', errors='ignore') as f:
            text = f.read()
        logger.info("[MarkdownReader] Successfully read MD file: {}".format(path))
        return text
    except Exception as e:
        raise SandyieException("Failed to read the .md file", e)

# def read_markdown(path):
#     """
#     Reads a Markdown file with extension `.markdown` and returns its content as a string.

#     :param path: Path to the `.markdown` file
#     :return: str – the raw Markdown text
#     """
#     try:
#         with io.open(path, 'r', encoding='utf-8', errors='ignore') as f:
#             text = f.read()
#         logger.info("[MarkdownReader] Successfully read MARKDOWN file: {}".format(path))
#         return text
#     except Exception as e:
#         raise SandyieException("Failed to read the .markdown file", e)
