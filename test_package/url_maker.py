from typing import Dict


class URLMaker:
    def __init__(self):
        self.base_url = None

    def set_base_url(self, url):
        self.base_url = url

    def add_query(self, query_object: Dict[str, str]):
        url_copy = self.base_url
        url_copy += "?"
        for i, (query, item) in enumerate(query_object.items()):
            url_copy += f"{query}={item}{'&' if i < len(query_object) - 1 else ''}"
        return url_copy
