from typing import Optional


class HttpResponse:
    def __init__(self, status_code: int, body: Optional[dict] = None) -> None:
        self.status_code = status_code
        self.body = body
