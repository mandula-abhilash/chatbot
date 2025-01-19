import logging

def setup_logging():
    """
    Configure the logging settings for the application.
    """
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
        handlers=[
            logging.FileHandler("app.log"),  # Logs to a file
            logging.StreamHandler()           # Logs to console
        ]
    )

    logger = logging.getLogger(__name__)
    logger.info("Logging is set up.")
    return logger

# Initialize logger globally
logger = setup_logging()
