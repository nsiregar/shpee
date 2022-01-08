from typing import List
from urllib.parse import urljoin, urlparse
import json


class ShortLink:
    def __init__(self, origin_url: str, sub_ids: List[str] = []):
        self.origin_url = self._clean_url(origin_url)
        self.sub_ids = sub_ids

    @property
    def payload(self):
        graphql_query = """mutation{{
            generateShortLink(input: {{
                originUrl: "{}",
                subIds: {}
            }}){{
                shortLink
            }}
        }}""".format(
            self.origin_url, json.dumps(self.sub_ids)
        )
        query_payload = {"query": graphql_query}
        return query_payload

    def _clean_url(self, url):
        clean_url = urljoin(url, urlparse(url).path)
        return clean_url
