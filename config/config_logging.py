# File: config_logging.py
# Author: BALL Alhousseynou
# Date: Thu Jun 23 2022

import logging
import os
from datetime import datetime


def initlogs(name_log: str):
    """
    Create logs directory if it doesn't exist
    Init logging
    """
    if not os.path.exists('logs'):
        os.makedirs('logs')

    set_logging_level(name_log)


def set_logging_level(name_log: str):
    """
    Setting the logger
    """
    log_level = "INFO"
    level = logging.INFO

    timestamp = str(datetime.now().strftime('%Y%m%d_%H%M%S'))
    file_path = f"logs/{timestamp}"
    file_path += f"_{name_log}.log" if name_log else ".log"

    logging.basicConfig(
        format='%(asctime)s - [%(levelname)s]: [%(filename)s] - %(message)s',
        level=level,
        filename=file_path
    )
    logging.info(f"Log level has been set to {log_level}")
