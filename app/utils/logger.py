import logging

def setup_logging():
    """
    Configure the logging settings for the application.
    """
    logging.basicConfig(
        level=logging.DEBUG,  # Changed to DEBUG level
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        handlers=[
            logging.FileHandler("app.log"),
            logging.StreamHandler(),
            logging.FileHandler("debug.log")  # Separate debug log file
        ]
    )

    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)  # Ensure logger level is DEBUG
    logger.info("Logging is set up with DEBUG level")
    return logger

# Initialize logger globally
logger = setup_logging()