from typing import List
# import bisect

import spacy

from doc_resolve import Page
nlp = spacy.load("en_core_web_sm")

class TextRecognition:
    """
    Named Entity Recognition from pages text
    """
    required_categories = {"ORG": "ORGANIZATION", "GPE": "LOCATION", "DATE": "DATE",
                           "MONEY": "MONEY", "PERSON": "PERSON"}

    def __init__(self, pages: List[Page]):
        self.labeled_data = []
        for page in pages:
            doc = nlp(page.text)
            tokens = (token for token in page.tokens)

            facts = []
            try:
                token = next(tokens)
                for text, label, start_char, end_char in self.yield_text_label_pos(doc.ents):
                    while token.offset < start_char:
                        facts.append({"text": token.text,
                                      "tag": "O",
                                      "tokens": token.to_dict()
                                      })
                        token = next(tokens)

                    fact = None
                    while start_char <= token.offset < end_char:
                        if fact is None:
                            fact = {"text": text,
                                    "tag": label,
                                    "tokens": []
                                    }
                        fact["tokens"].append(token.to_dict())

                        token = next(tokens)
                    if fact is not None:
                        facts.append(fact)
                else:
                    while True:
                        facts.append({"text": token.text,
                                      "tag": "O",
                                      "tokens": token.to_dict()
                                      })
                        token = next(tokens)

            except StopIteration:
                # all tokens is processed
                pass

            self.labeled_data.append({"facts": facts,
                                      "source": page.source})

    def to_dict(self):
        return self.labeled_data

    @staticmethod
    def yield_text_label_pos(entities):
        for ent in entities:
            if ent.label_ in TextRecognition.required_categories:
                label = TextRecognition.required_categories[ent.label_]
            else:
                label = "O"
            yield ent.text, label, ent.start_char, ent.start_char + len(ent.text)


"""
{

"facts": [

{

"text": "Bob Ross",

"tag": "PERSON",

"tokens": [

{

"text": "Bob",

"position": {

"left": 0.0,

"top": 0.0,

"width": 6.1,

"height": 1.2

}

"offset": 0

},

{

"text": "Ross",

"position": {

"left": 7.0,

"top": 0.0,

"width": 3.1,

"height": 1.2

}

"offset": 4

}

]

},

... ну и так далее

]

"source": {

"width": 250,

"height": 250

}

}
"""






