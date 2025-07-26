import os

def get_file_extension(file_path: str) -> str:
    """
    Extract the file extension from a file path.
    
    Args:
        file_path (str): Path to the file.

    Returns:
        str: File extension (e.g., '.csv', '.json').
    """
    _, ext = os.path.splitext(file_path)
    return ext.lower()


def is_valid_file(file_path: str) -> bool:
    """
    Check if the file exists and is a file.

    Args:
        file_path (str): Path to the file.

    Returns:
        bool: True if valid file, False otherwise.
    """
    return os.path.isfile(file_path)
