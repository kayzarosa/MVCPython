class HttpRequest:
    def __init__(self, body: dict = None, param: dict = None) -> None:  # type: ignore
        self.body = body
        self.param = param
