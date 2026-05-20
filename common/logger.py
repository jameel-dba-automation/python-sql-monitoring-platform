import logging
from pathlib import Path


def setup_logger():

    # Get project root directory
    BASE_DIR = Path(__file__).resolve().parent.parent

    # Logs folder path
    log_folder = BASE_DIR / 'logs'

    # Create logs folder if not exists
    log_folder.mkdir(exist_ok=True)

    # Log file path
    log_file = log_folder / 'monitoring.log'

    # Configure logger
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler(log_file),
            logging.StreamHandler()
        ]
    )

    return logging