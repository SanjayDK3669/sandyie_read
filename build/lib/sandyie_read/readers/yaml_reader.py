import yaml
from sandyie_read.logging_config import logger

def read_yaml(file_path):
    """Read data from a YAML file."""
    try:
        with open(file_path, 'r') as file:
            data = yaml.safe_load(file)
            logger.info(f"YAML file read successfully: {file_path}")
            return data
    except Exception as e:
        logger.error(f"Error reading YAML file: {e}")
        return None
