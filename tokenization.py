# tokenization.py

import spacy

nlp = spacy.load('en_core_web_sm')

def spacy_tokenize(text):
    doc = nlp(text)
    return [token.text for token in doc]
