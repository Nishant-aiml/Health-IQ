import logging
import json
import sys
from datetime import datetime, timezone
from backend.app.core.config import settings


class UnbufferedStreamHandler(logging.StreamHandler):
    """
    StreamHandler that immediately flushes every log record.
    Prevents log loss in cloud container environments like Render.
    """

    def emit(self, record: logging.LogRecord) -> None:
      super().emit(record)
      self.flush()


class JSONFormatter(logging.Formatter):
    """
    Custom JSON log formatter for structured application logging.
    """

    def format(self, record: logging.LogRecord) -> str:
      log_object = {
          "timestamp": datetime.now(timezone.utc).isoformat(),
          "level": record.levelname,
          "logger": record.name,
          "message": record.getMessage(),
          "module": record.module,
          "func_name": record.funcName,
          "line_no": record.lineno,
      }

      # Attach extra contextual properties if available
      if hasattr(record, "request_id"):
        log_object["request_id"] = getattr(record, "request_id")
      if hasattr(record, "method"):
        log_object["method"] = getattr(record, "method")
      if hasattr(record, "path"):
        log_object["path"] = getattr(record, "path")
      if hasattr(record, "status_code"):
        log_object["status_code"] = getattr(record, "status_code")
      if hasattr(record, "duration_ms"):
        log_object["duration_ms"] = getattr(record, "duration_ms")

      if record.exc_info:
        log_object["exception"] = self.formatException(record.exc_info)

      return json.dumps(log_object)


def setup_logger() -> logging.Logger:
    logger = logging.getLogger("health_companion")
    logger.setLevel(getattr(logging, settings.LOG_LEVEL.upper(), logging.INFO))

    handler = UnbufferedStreamHandler(sys.stdout)
    if getattr(settings, "LOG_FORMAT", "json").lower() == "text":
      handler.setFormatter(
          logging.Formatter("%(asctime)s [%(levelname)s] %(name)s: %(message)s")
      )
    else:
      handler.setFormatter(JSONFormatter())

    if not logger.handlers:
      logger.addHandler(handler)

    logger.propagate = False
    return logger


logger = setup_logger()

