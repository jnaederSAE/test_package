from typing import Dict
from urllib.parse import urlencode, quote


class URLMaker:
    def __init__(self, base_url: str = None) -> None:
        self._base_url = base_url
        self._working_url = None

    def get_base_url(self) -> str:
        return self._base_url

    def set_base_url(self, url: str) -> None:
        self._base_url = url

    def new_url(self) -> 'URLMaker':
        self._working_url = self._base_url
        return self

    def add_query(self, query_object: Dict[str, str]) -> 'URLMaker':
        self._working_url += f"?{urlencode(query_object)}"
        return self

    def add_path(self, path_name: str) -> 'URLMaker':
        self._working_url += f"/{quote(path_name)}"
        return self

    def end_url(self) -> str:
        output = self._working_url
        self._working_url = None
        return output
