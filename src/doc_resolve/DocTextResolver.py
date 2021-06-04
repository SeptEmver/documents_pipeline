import json
from typing import Dict, List, Tuple, Any

from pandas import DataFrame
import pytesseract
from pytesseract import Output

from tools.ExceptionsWithCodes import ServerError
from .Document import MultiDocument
from .Area import Area
from .Page import Page
from .Token import Token

# Костыль, да. Пропустил PATH галочку при установке. А с PATH указывал tesseract, но остаётся проблема
import socket
if socket.gethostname() == "kara":
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

class DocTextResolver:
    """
    Извлекает из изображения текстовую информацию
    Требует установленного Tesseract
    """

    def __init__(self, multi_doc: MultiDocument):
        self.multi_doc = multi_doc
        img_array = multi_doc.pages
        if not img_array:
            raise ServerError("Received empty image array for text resolve")
        custom_config = r'--oem 3 --psm 6'
        self.data_array: List[DataFrame] = []
        for img in img_array:
            self.data_array.append(pytesseract.image_to_data(img, output_type=Output.DATAFRAME, config=custom_config,
                                                             pandas_config={"usecols": ["left", "top", "width", "height", "conf", "text"]}
                                                             ))

    def reduce_data_with_conf_less_than(self, confidence=40):
        for i in range(len(self.data_array)):
            self.data_array[i] = self.data_array[i].where(self.data_array[i]["conf"] > confidence)
            self.data_array[i].dropna(subset=["text"], inplace=True)

    def process(self) -> List[Page]:
        """
        Извлекает структуру (текст страницы, токены, размер изображения документа) для каждой страницы
        """
        pages = []
        for i, data, (_, info) in zip(range(len(self.data_array)), self.data_array, self.multi_doc):
            text = " ".join(str(x[1]) for x in data["text"].iteritems())
            tokens = []
            offset = 0
            for (_, (left, top, width, height, s)) in \
                    data[["left", "top", "width", "height", "text"]].iterrows():
                s = str(s)
                tokens.append(Token(s, Area(left, top, width, height), offset))
                offset += len(s) + 1
            source = {"width": info["width"], "height": info["height"]}
            pages.append(Page(text, tokens, source))
        return pages

    def to_dict(self, pages: List[Page] = None) -> Dict:
        if pages is None:
            pages = self.process
        pages_data = []
        for page in pages:
            pages_data.append(page.to_dict())
        return {"pages": pages_data}

    def to_json(self) -> str:
        return json.dumps(self.to_dict())



"""
    {

"text": "Какой-то извлеченный текст"

"tokens": [

{

"text": "Какой-то",

"position": {

"left": 0.0,

"top": 0.0,

"width": 6.1,

"height": 1.2

}

"offset": 0

},

{

"text": "извлеченный",

"position": {

"left": 0.0,

"top": 0.0,

"width": 6.1,

"height": 1.2

}

"offset": 9

}

... тут остальные слова

]

"source": {

"width": 250,

"height": 250

}

}"""


