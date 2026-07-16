import os

import logging


def setup_logging() -> None:
    """
    Set up logging for the app
    :return: None
    """

    os.makedirs("/app/logs", exist_ok=True)  # use absolute path in Docker

    logger = logging.getLogger()  # root logger
    logger.setLevel(logging.INFO)
    logging.getLogger("watchfiles").setLevel(logging.WARNING)

    file_handler = logging.FileHandler("/app/logs/app.log")
    file_handler.setFormatter(
        logging.Formatter("%(asctime)s %(levelname)s [%(name)s] %(message)s")
    )
    logger.addHandler(file_handler)
