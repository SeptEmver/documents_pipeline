import os
import json
import tempfile
from typing import Tuple, Dict

from werkzeug.datastructures import FileStorage

from doc_resolve import DocFormatValidator, DocPreprocessor, DocTextResolver, MultiDocument
from NER_resolve import TextRecognition
from tools.ExceptionsWithCodes import ClientError, ServerError



def handle_multi_doc(doc_file: FileStorage) -> Dict:
    """
    один общий метод для обработки документа, на вход которого будет поступать сам документ (многостраничный tiff). В процессе обработки:
    из него будет извлекаться текст (задание 1);
    графические объекты (задание 2);
    тексты страниц будут классифицировать на первые и не первые (задание 3);
    из первых страниц будут извлечены значимые факты (задание 4);
    :param doc_file: uploaded image file with request information
    :return: json
    """

    "Task 1"

    if not DocFormatValidator(doc_file):
        raise ServerError("Failed to validate document format")

    try:
        # Необходимо записывать в файл, потому что cv2.imreadmulti читает только из файла, но не из буфера
        # Если внутри with.. то временный файл просто не процессится img=None, быстро установить причину не удалось. Возможно блокировка
        with tempfile.NamedTemporaryFile(mode='w+b', suffix=".tiff", delete=False) as temp_file:
            buffer = doc_file.stream.read()
            temp_file.write(buffer)

        multi_doc = MultiDocument(temp_file.name)

        docPreprocessor = DocPreprocessor(multi_doc)
        preprocessed_multi_doc = docPreprocessor.preprocess()

    except Exception as e:
        raise e
    finally:
        if os.path.exists(temp_file.name):
            os.remove(temp_file.name)

    doc_text = DocTextResolver(preprocessed_multi_doc)
    doc_text.reduce_data_with_conf_less_than(40)
    pages_tokenized = doc_text.process()

    task_1_result_dict = doc_text.to_dict(pages_tokenized)

    "Task 2 - not implemented"
    task_2_result_dict = {}

    "Task 3 - not implemented"
    task_3_result_dict = {
            "source": {
                "width": None,
                "height": None,
                "type": "other"
            }
        }

    "Task 4"

    text_rec = TextRecognition(pages_tokenized)
    task_4_result_dict = text_rec.to_dict()

    return {"task_1": task_1_result_dict,
            "task_2": task_2_result_dict,
            "task_3": task_3_result_dict,
            "task_4": task_4_result_dict}
