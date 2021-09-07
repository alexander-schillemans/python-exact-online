from .base import BaseModel

class Error(BaseModel):

    def __init__(self,
        code=None,
        message=None,
    ):

        self.code = code
        self.message = message