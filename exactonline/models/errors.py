from .base import BaseModel

class Error(BaseModel):

    def __init__(self,
        http_status=None,
        code=None,
        message=None,
    ):

        self.http_status = http_status
        self.code = code
        self.message = message