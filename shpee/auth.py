import hashlib
import datetime
import calendar
import json


class Authentication:
    def __init__(self, app_id: str, app_secret: str):
        self.app_id = app_id
        self.app_secret = app_secret
        self.current_time = datetime.datetime.utcnow()
        self.timestamp = calendar.timegm(self.current_time.utctimetuple())

    def signature(self, payload: str) -> str:
        payload = json.dumps(payload)
        signature = f"{self.app_id}{self.timestamp}{payload}{self.app_secret}"
        hashing = hashlib.sha256(signature.encode("utf-8"))
        return hashing.hexdigest()
