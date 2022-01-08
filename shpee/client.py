from typing import List
from httpx import Client
from .auth import Authentication
from .shortlink import ShortLink


class ShopeeClient:
    base_url = "https://open-api.affiliate.shopee.co.id"

    def __init__(self, app_id: str, app_secret: str):
        self.app_id = app_id
        self.app_secret = app_secret
        self._client = Client(base_url=self.base_url)

    def post(self, payload: str):
        headers = self._headers(payload)
        return self._client.post("/graphql", headers=headers, json=payload)

    def _headers(self, payload):
        auth = Authentication(self.app_id, self.app_secret)
        headers = {
            "Authorization": f"SHA256 Credential={auth.app_id}, Signature={auth.signature(payload)}, Timestamp={auth.timestamp}",
            "Content-Type": "application/json",
        }
        return headers


class ShopeeAffiliate:
    def __init__(self, app_id: str, app_secret: str):
        self._client = ShopeeClient(app_id=app_id, app_secret=app_secret)

    def shortlink(self, origin_url: str, sub_ids: List[str] = []):
        link = ShortLink(origin_url=origin_url, sub_ids=sub_ids)
        resp = self._client.post(payload=link.payload)
        return resp
