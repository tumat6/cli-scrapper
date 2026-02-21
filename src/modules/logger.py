import json
import logging
from pathlib import Path


class JsonFormatter(logging.Formatter):
    def format(self, record: logging.LogRecord) -> str:
        payload = {
            "asctime": self.formatTime(record, self.datefmt),
            "levelname": record.levelname,
            "name": record.name,
            "message": record.getMessage(),
        }
        reserved = set(logging.makeLogRecord({}).__dict__.keys())
        for key, value in record.__dict__.items():
            if key not in reserved and key not in payload:
                payload[key] = value
        return json.dumps(payload, ensure_ascii=True)


def setup_logging(level: int = logging.INFO, log_file: str = "logs_pipeline.json") -> None:
    root_logger = logging.getLogger()

    if root_logger.handlers:
        return

    root_logger.setLevel(level)
    Path(log_file).touch(exist_ok=True)

    formatter = JsonFormatter()

    file_handler = logging.FileHandler(log_file, encoding="utf-8")
    file_handler.setFormatter(formatter)

    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)

    root_logger.addHandler(file_handler)
    root_logger.addHandler(stream_handler)


def get_logger(name: str) -> logging.Logger:
    return logging.getLogger(name)
