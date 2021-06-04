from typing import List

from .Token import Token

class Page:
    def __init__(self, text, tokens, source):
        self.text = text
        self.tokens: List[Token] = tokens
        self.source = source

    def to_dict(self):
        tokens_struct = []
        for token in self.tokens:
            tokens_struct.append(token.to_dict())
        return {"text": self.text,
                "tokens": tokens_struct,
                "source": self.source}
