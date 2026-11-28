import json
import uuid
from datetime import datetime, timezone
import logging
import os

from flask import request
from flask_login import current_user

os.makedirs("logs", exist_ok=True)

_handler = logging.FileHandler("logs/audit.jsonl", encoding="utf-8")
_handler.setFormatter(logging.Formatter("%(message)s"))

_logger = logging.getLogger("audit")
_logger.setLevel(logging.INFO)
_logger.addHandler(_handler)


def log_action(action, result, object_type=None, object_id=None, reason_code=None):
    if current_user.is_authenticated:
        actor_id = current_user.id
        actor_role = current_user.role
    else:
        actor_id = None
        actor_role = "anonymous"
    event = {
        "timestamp": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "schema_version": 1,
        "event_id": "evt-" + uuid.uuid4().hex,
        "action": action,
        "result": result,
        "actor_id": actor_id,
        "actor_role": actor_role,
        "object_type": object_type,
        "object_id": object_id,
        "reason_code": reason_code,
        "src_ip": request.remote_addr,
        "http_method": request.method,
        "route": request.url_rule.rule if request.url_rule else None,
    }
    _logger.info(json.dumps(event))