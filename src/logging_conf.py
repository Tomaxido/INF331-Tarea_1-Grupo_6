import logging

logger = logging.getLogger("event_cli")
logger.setLevel(logging.INFO)

if not logger.handlers:
    fh = logging.FileHandler("app.log", encoding="utf-8")
    fmt = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
    fh.setFormatter(fmt)
    fh.setLevel(logging.INFO)
    logger.addHandler(fh)
