from typing import List
import cv2
from tools.ExceptionsWithCodes import ServerError

class MultiDocument:
    """
    Multi page(.tiff-like) image and additional data representation
    """

    def __init__(self, doc_file_path: str, mats=(), flags=cv2.IMREAD_COLOR):
        status, self.pages = cv2.imreadmulti(doc_file_path, mats, flags)
        if not status:
            raise ServerError('Failed to load document image')

        self.info: List = []
        for i, page in enumerate(self.pages):
            self.info.append({})
            self.info[i]["height"], self.info[i]["width"], _ = page.shape
        assert len(self.pages) == len(self.info)

    def __iter__(self):
        return zip(self.pages, self.info)
