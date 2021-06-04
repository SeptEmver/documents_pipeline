from .Area import Area

class Token:
    def __init__(self, text: str, position: Area, offset: int, ):
        self.text = text
        self.position = position
        self.offset = offset


    def to_dict(self):
        return {"text": self.text,
                "position": self.position.to_dict(),
                "offset": self.offset
                }


