from tools.ExceptionsWithCodes import ClientError


class DocFormatValidator:
    """Make sure that we have accepted correct format"""
    def __init__(self, doc_file):
        self.status = False
        if doc_file.content_type == 'image/tiff' or doc_file.content_type == 'image/tif':
            self.status = True
        elif doc_file.content_type.startswith('image'):
            raise ClientError("Unsupported image format")
        else:
            raise ClientError("Not expected type of data")

    def __bool__(self):
        return self.status
