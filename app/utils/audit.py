import logging
import os

from flask import request
from flask_login import current_user

os.makedirs("logs", exist_ok=True)

_handler = logging.FileHandler("logs/app.log", encoding="utf-8")
_handler.setFormatter(logging.Formatter("%(asctime)s %(message)s"))

_logger = logging.getLogger("audit")
_logger.setLevel(logging.INFO)
_logger.addHandler(_handler)


def log_action(action):
    if current_user.is_authenticated:
        user = current_user.username
    else:
        user = "anonymous"
    _logger.info(
        "user=%s ip=%s action=%s path=%s",
        user,
        request.remote_addr,
        action,
        request.path,
    )