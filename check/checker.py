import requests


class Checker:
    def __init__(self, url: str):
        self.url = url

    def _check(self) -> int:
        return requests.get(self.url).status_code

    @property
    def status_code(self):
        try:
            return self._check()
        except requests.exceptions.ConnectionError:
            return 404
