class HttpError(Exception):
    def __init__(self, status_code: int, status: str, message: str = None, detail: str = None):
        self.status_code = status_code
        self.status = status
        self.message = message or "An error occurred"
        self.detail = detail