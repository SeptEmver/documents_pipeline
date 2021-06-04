from tools.ExceptionsWithCodes import ServerError

class Area:
    """
    Area image representation
    """
    def __init__(self, left, top, width, height):
        self.left = left
        self.top = top
        self.width = width
        self.height = height

    def __add__(self, other):
        if not isinstance(other, Area):
            raise ServerError("Wrong Area object for concatenation")
        left_min = min(self.left, other.left)
        top_min = min(self.top, other.top)
        left_max = max(self.left + self.width, other.left + other.width)
        top_max = max(self.top + self.height, other.top + other.height)
        return Area(left_min, top_min,
                    left_max - left_min,
                    top_max - top_min)

    def __eq__(self, other):
        return self.left == other.left and \
               self.top == other.top and \
               self.width == other.width and \
               self.height == other.height

    def to_dict(self):
        return {"left": self.left,
                "top": self.top,
                "width": self.width,
                "height": self.height
                }
