import logging.config
import logging.handlers
import pathlib
import atexit
import json


logger = logging.getLogger("ecg_app")

class ECGLogger:
    def __init__(self, level="INFO") -> None:
        logging.basicConfig(level=level)
        config_file = pathlib.Path("app/utils/logger_config.json")
        with open(config_file) as f_in:
            config = json.load(f_in)

        logging.config.dictConfig(config)

