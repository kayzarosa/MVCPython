from typing import Optional


class HttpRequest:
    def __init__(
        self, body: Optional[dict] = None, param: Optional[dict] = None
    ) -> None:
        self.body = body
        self.param = param
