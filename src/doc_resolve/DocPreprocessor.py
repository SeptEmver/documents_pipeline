import cv2
import numpy as np
from .Document import MultiDocument
from functools import reduce


class DocPreprocessor:
    """Preprocess loaded image"""
    def __init__(self, multi_doc: MultiDocument):
        self.multi_doc = multi_doc
        self.doc_img_array = multi_doc.pages

    # def __bool__(self):
    #     return self.status

    def preprocess(self):
        """
        :return: cv2 Image
        """
        self.pr_get_grayscale()
        self.pr_thresholding()
        # self.pr_remove_noise()
        # self.pr_opening()
        return self.multi_doc

    # get grayscale image
    def pr_get_grayscale(self):
        for i in range(len(self.doc_img_array)):
            self.doc_img_array[i] = cv2.cvtColor(self.doc_img_array[i], cv2.COLOR_BGR2GRAY)

    # noise removal
    def pr_remove_noise(self, blur_width=2):
        for i in range(len(self.doc_img_array)):
            self.doc_img_array[i] = cv2.medianBlur(self.doc_img_array[i], blur_width)

    # thresholding
    def pr_thresholding(self):
        for i in range(len(self.doc_img_array)):
            self.doc_img_array[i] = cv2.threshold(self.doc_img_array[i], 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

    # opening - erosion followed by dilation
    def pr_opening(self):
        kernel = np.ones((5, 5), np.uint8)
        for i in range(len(self.doc_img_array)):
            self.doc_img_array[i] = cv2.morphologyEx(self.doc_img_array[i], cv2.MORPH_OPEN, kernel)

    # def get_all_preprocess_methods(self):
    #     return [self.__getattribute__(x) for x in dir(DocPreprocessor) if x.startswith("pr_")]

    def write_to_file(self, file):
        return cv2.imwritemulti(file, self.doc_img_array)
